pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '--privileged'  // Для Docker-in-Docker
        }
    }

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        OPENCART_URL = "http://opencart:8080"
        SELENOID_URL = "selenoid:4444"
        BROWSER = "chrome"
        BROWSER_VERSION = "latest"
    }


    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Meliodaus957/OPENCART_SELENIUM'
            }
        }

        stage('Install Docker Compose') {
            steps {
                script {
                    sh '''
                        if ! command -v docker-compose &> /dev/null; then
                            curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
                            chmod +x /usr/bin/docker-compose
                        fi
                    '''
                }
            }
        }

        stage('Start Services') {
            steps {
                script {
                    // Запуск контейнеров с OpenCart и Selenoid
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'

                    // Ожидание готовности OpenCart (пример с curl)
                    sh '''
                    echo "Waiting for OpenCart to be ready..."
                    until curl -s ${OPENCART_URL} > /dev/null; do
                        echo "Waiting for OpenCart..."
                        sleep 5
                    done
                    echo "OpenCart is up and running!"
                    '''
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    // Установка виртуального окружения
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'

                    // Установка зависимостей
                    sh 'pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск тестов внутри виртуального окружения
                    sh '''
                    . venv/bin/activate
                    pytest -v tests/test_opencart.py --alluredir=allure-results \
                        --base_url=${OPENCART_URL} --browser=${BROWSER} \
                        --bv=${BROWSER_VERSION} --executor=${SELENOID_URL}
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    sh 'allure generate allure-results --clean -o allure-report'
                    sh 'allure open allure-report'
                }
            }
        }
    }

    post {
        always {
            script {
                // Остановка контейнеров после завершения тестов
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
            }
        }
    }
}

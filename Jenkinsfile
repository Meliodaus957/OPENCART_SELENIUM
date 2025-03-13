pipeline {
    agent any
    parameters {
        string(name: 'EXECUTOR', defaultValue: 'selenoid', description: 'Адрес Selenoid')
        string(name: 'BASE_URL', defaultValue: 'http://opencart:8080', description: 'Адрес OpenCart')
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Браузер')
        string(name: 'BV', defaultValue: 'latest', description: 'Версия браузера')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Meliodaus957/OPENCART_SELENIUM.git',
                    credentialsId: 'b8598cbf-4b65-4202-a7f3-42b9d10afab2'
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                    apt-get update && apt-get install -y python3 python3-pip python3.11-venv
                '''
            }
        }


        stage('Install Allure') {
            steps {
                script {
                    // Установка Allure с использованием Homebrew
                    sh 'brew install allure'
                }
            }
        }


        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate  # Активируем виртуальное окружение
                    pip install -r requirements.txt
                '''
            }
        }


        stage('Set up environment') {
            steps {
                script {
                    // Устанавливаем Docker Compose
                    sh 'apt-get update'
                    sh 'apt-get install -y docker-compose'
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate  # Снова активируем виртуальное окружение перед запуском тестов
                    pytest tests --alluredir=allure-results \
                    --executor=${EXECUTOR} \
                    --base_url=${BASE_URL} \
                    --browser=${BROWSER} \
                    --bv=${BV}
                '''
            }
        }


        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results --clean -o allure-report'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results']]
            }
        }
    }
}

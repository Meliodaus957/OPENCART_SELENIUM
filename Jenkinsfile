pipeline {
    agent any

    environment {
        OPENCART_URL = "http://opencart:8080"
        SELENOID_URL = "http://selenoid:4444/wd/hub"
        BROWSER = "chrome"
        BROWSER_VERSION = "latest"
        THREADS = "2"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Meliodaus957/OPENCART_SELENIUM'
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    // Установка Python и pip
                    sh 'apt-get update'
                    sh 'apt-get install -y python3 python3-pip'

                    // Установка зависимостей из requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запускаем тесты с нужными параметрами
                    sh 'pytest -n ${THREADS} --alluredir=allure-results --opencart_url ${OPENCART_URL} --browser ${BROWSER} --browser_version ${BROWSER_VERSION} --executor ${SELENOID_URL}'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Генерация отчета Allure
                    sh 'allure generate allure-results --clean -o allure-report'
                    sh 'allure open allure-report'
                }
            }
        }
    }
}

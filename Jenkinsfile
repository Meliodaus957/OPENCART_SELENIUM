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

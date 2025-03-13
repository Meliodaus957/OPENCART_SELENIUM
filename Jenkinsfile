pipeline {
    agent any
    parameters {
        string(name: 'EXECUTOR_URL', defaultValue: 'http://localhost:4444/wd/hub', description: 'Адрес Selenoid')
        string(name: 'OPENCART_URL', defaultValue: 'http://localhost:8080', description: 'Адрес OpenCart')
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Браузер')
        string(name: 'BROWSER_VERSION', defaultValue: 'latest', description: 'Версия браузера')
        string(name: 'THREADS', defaultValue: '2', description: 'Количество потоков')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your_repo/opencart-tests.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    pytest tests --alluredir=allure-results \
                    --executor-url=${EXECUTOR_URL} \
                    --opencart-url=${OPENCART_URL} \
                    --browser=${BROWSER} \
                    --browser-version=${BROWSER_VERSION} \
                    --threads=${THREADS}
                '''
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results -o allure-report --clean'
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results']]
            }
        }
    }
}

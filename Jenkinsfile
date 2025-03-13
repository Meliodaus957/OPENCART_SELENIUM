pipeline {
    agent any
    parameters {
        string(name: 'EXECUTOR', defaultValue: 'host.docker.internal', description: 'Адрес Selenoid')
        string(name: 'BASE_URL', defaultValue: 'http://192.168.0.112:8081/', description: 'Адрес OpenCart')
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Браузер')
        string(name: 'BV', defaultValue: 'latest', description: 'Версия браузера')
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
                    --executor=${EXECUTOR} \
                    --base_url=${BASE_URL} \
                    --browser=${BROWSER} \
                    --bv=${BV} \
                    --threads=${THREADS}
                '''
            }
        }
        stage('Generate Allure Report

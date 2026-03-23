pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t uptime-monitor .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f uptime-monitor || exit 0'
                bat 'docker run -d -p 5000:5000 --name uptime-monitor uptime-monitor'
            }
        }

        stage('Wait for App') {
            steps {
                sleep time: 10, unit: 'SECONDS'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'pip install selenium webdriver-manager'
                bat 'python test_uptime.py'
            }
        }

        stage('Cleanup') {
            steps {
                bat 'docker stop uptime-monitor'
                bat 'docker rm uptime-monitor'
            }
        }
    }
}
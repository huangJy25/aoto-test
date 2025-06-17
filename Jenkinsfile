pipeline {
    agent any

    environment {
        PYTHON = 'D:\\test\\Python\\python.exe'
    }

    stages {
        stage('拉取代码') {
            steps {
                git url: 'https://github.com/huangJy25/aoto-test.git', branch: 'main'
            }
        }

        stage('安装依赖') {
            steps {
                bat "${env.PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('执行测试') {
            steps {
                bat "${env.PYTHON} -m pytest TestApi/ --alluredir=allure-results"
            }
        }

        stage('生成 Allure 报告') {
            steps {
                bat 'allure generate allure-results -o allure-report --clean'
            }
        }

        stage('发布 Allure 报告') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
            }
        }
    }
}

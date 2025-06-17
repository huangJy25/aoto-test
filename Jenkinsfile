pipeline {
    agent any   // 使用任意可用节点

    stages {
//         stage('Clone Code') {
//             steps {
//                 // 克隆 Git 仓库（如果你使用 Pipeline from SCM 则不需要这一步）
//                 git 'https://github.com/你的用户名/你的仓库.git'
//             }
//         }

        stage('Install Dependencies') {
            steps {
                // 安装依赖
                bat '"D:\\test\\Python\\python.exe" -m pip install -r D:\\test\\Python_test\\py_test_4\\requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // 执行 Pytest 自动化测试
                bat '"D:\\test\\Python\\python.exe" -m pytest D:\\test\\Python_test\\py_test_4\\TestApi\\ --alluredir=D:\\test\\Python_test\\py_test_4\\allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                // 生成 Allure 报告
                bat 'allure generate D:\\test\\Python_test\\py_test_4\\allure-results -o D:\\test\\Python_test\\py_test_4\\allure-report --clean'
            }
        }

        stage('Publish Report') {
            steps {
                // 发布 HTML 报告到 Jenkins 页面（需安装 HTML Publisher Plugin 插件）
                publishHTML(target: [
                    reportDir: 'D:\\test\\Python_test\\py_test_4\\allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
            }
        }
    }
}
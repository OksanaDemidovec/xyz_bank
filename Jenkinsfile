pipeline {
    agent {
        docker {
            image 'docker.io/lyubavablago/pythongirlpower:pythongirlpower'
            args '-u root:root'
        }
    }
    triggers {
      cron 'H 7 16 * *'
    }
    tools {
      allure 'ALLURE'
    }

    stages {
        stage('Preparation') {
            steps {
                script {
                    echo 'Install packages'
                    sh '''
                        apt-get update
                        wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.17.2/allure-commandline-2.17.2.tgz -O /tmp/allure-commandline.tgz
                        tar -zxvf /tmp/allure-commandline.tgz -C /opt/
                        ln -s /opt/allure-2.17.2/bin/allure /usr/bin/allure
                    '''
                }
            }
        }
    }

        post {
            always {
                script {
                    if (fileExists('./pythongirlpower/allure-results')) {
                        echo 'Generating Allure report'
                        sh 'allure generate ./pythongirlpower/allure-results --clean -o pythongirlpower/allure-report'
                        archiveArtifacts artifacts: 'pythongirlpower/allure-results/**', allowEmptyArchive: true
                        archiveArtifacts artifacts: 'pythongirlpower/allure-report/**', allowEmptyArchive: true
                    } else {
                    echo 'Allure results not found.'
                }
            }
        }
    }
}
pipeline {
    agent any

    tools {
        nodejs "NodeJS"
    }

    stages {
        stage('Build') {
            steps {
                sh 'npm install -g npm'
                sh 'npm --version'
                sh 'node --version'
            }
        }
        stage('Test Post board requests') {
            steps {
            
                    sh '''#!/bin/bash
                    
                    npm --version; 
                    node --version;
                    echo "------> Install node modules <-------";
                    npm install -g newman;
                    npm install -g newman-reporter-htmlextra
                    echo "----running postman tests----";
                    echo "running post board request tests";
                    newman run "https://www.getpostman.com/collections/c0ada7842e42e2618388" --delay-request 5000 --reporters cli,junit,htmlextra --reporter-junit-export "newman/postreq-test-report.xml" ;
                    '''

            }
        }
        stage('Test User Requests') {
            steps {

                sh '''#!/bin/bash
                    
                npm --version; 
                node --version;
                echo "------> Install node modules <-------";
                npm install -g newman;
                npm install -g newman-reporter-htmlextra
                echo "----running postman tests----";
                echo "running post board request tests";
                newman run "https://www.getpostman.com/collections/e3532e5c25dce3ef3ead" --delay-request 5000 --reporters cli,junit,htmlextra --reporter-junit-export "newman/userreq-integration-test-report.xml" ;
                '''
            }
        }
        //
        //stage('Push to Staging') {
        //    steps {
        //        script {
        //            if (env.BRANCH_NAME == 'master') {
        //                echo 'Current Branch: ' + env.GIT_BRANCH
        //                withCredentials([usernamePassword(credentialsId: '82d6b20c-0b65-4a42-8707-f44c0613558e', passwordVariable: 'L0v31987#', usernameVariable: 'omikrom')]) {
        //                sh('git add .')
        //                sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/omikrom/web-service-automated-testing.git')
        //                }
        //            } else {
        //                echo 'Current Branch: ' + env.GIT_BRANCH
        //                sh('hello')
        //            }
        //        }
        //    }
        //}
    }
}
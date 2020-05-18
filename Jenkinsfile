pipeline {
	agent {
		docker {
			image 'python'
		}
	}
	stages {
		stage('Build') {
			steps {
				sh 'pip install -r requirements.txt'
				sh 'python setup.py develop'
			}
		}
		stage('Test') {
			steps {
				sh 'pytest'
			}
			post {
				always {
					junit 'test-reports/*.xml'
				}
			}
		}
	}
}

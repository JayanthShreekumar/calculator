pipeline {
	agent {
		docker {
			image 'python'
		}
	}
	stages {
		stage('Build') {
			steps {
				sh 'python setup.py build'
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

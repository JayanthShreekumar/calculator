pipeline {
	agent {
		docker {
			image 'python'
		}
	}
	stages {
		stage('Build') {
			steps {
				sh 'python src/calc/Calculator.py'
			}
		}
		stage('Test') {
			steps {
				sh 'pytest --junit-xml=pytest_unit.xml'
			}
			post {
				always {
					junit '*.xml' 
				}
			}
		}
	}
}

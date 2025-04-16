# speech-to-text-transcriber
I built a fully serverless, cloud-native speech-to-text web tool using Google Cloud Platform (GCP) and modern frontend tech. The goal was to deliver fast, multilingual transcription with no local processing.

The frontend, built with HTML5, JavaScript, and CSS3, supports audio recording/upload via the MediaRecorder API and fetch requests. It features a clean, responsive UI that works across devices.

The backend uses Python (Flask), containerized with Docker, and deployed on Google Cloud Run for auto-scaling. It integrates Google Cloud Speech-to-Text API for real-time transcription and uses secure GCP service account authentication.

Firebase Hosting serves the frontend globally via CDN, enabling low-latency user access. The entire process—from audio input to cloud-based transcription—is handled seamlessly in the cloud, showcasing scalable cloud and web development.

deployed tool link: https://cloud-project-456204.web.app/homepage.html

# speech-to-text-transcriber
For this project, I developed a fully serverless, cloud-native speech-to-text transcription web tool using a combination of Google Cloud Platform (GCP) services and frontend technologies (HTML5, JavaScript, and CSS3). The objective was to create an accessible, fast, and multilingual transcription service that requires no local processing.

On the frontend, I used HTML5 to structure a responsive user interface that includes audio recording and file upload capabilities. JavaScript was central to handling user interactions — including capturing microphone input using the MediaRecorder API, managing audio playback, and sending audio data to the backend using asynchronous fetch requests. The UI was styled using CSS3 to deliver a clean and responsive design, ensuring it worked seamlessly across devices.

On the backend, I used Python with Flask, containerized the application using Docker, and deployed it using Google Cloud Run — a serverless platform that auto-scales based on demand. The Google Cloud Speech-to-Text API was integrated to perform real-time audio transcription in multiple languages. Authentication was securely handled using GCP service accounts.

For deployment and user access, I used Firebase Hosting, which served the frontend files globally with low latency via Google’s CDN. The entire workflow — from uploading or recording audio, sending it to the backend, processing it in the cloud, and returning the transcription — is hosted completely on the cloud.

By combining powerful cloud infrastructure (GCP) with responsive and intuitive web technologies (HTML5, JavaScript, and CSS3), I built a modern, scalable, and user-friendly tool that demonstrates practical, real-world application of both cloud and web development skills.

deployed tool link: https://cloud-project-456204.web.app/homepage.html

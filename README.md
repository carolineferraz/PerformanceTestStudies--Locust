<h3 align="center">🌿 Performance Test with Locust 🌿</h3>

<br>
<h6>• Install Python</h6>

<h6>• Clone repository</h6>

<h6>• Create Python Virtual Environment:</h6>
<pre>python -m venv venv</pre>

<h6>• Install Locust:</h6>
<pre>pip install locust</pre>

<h6>• Run Locust:</h6>
<pre>locust -f performanceTests.py</pre>

<h6>• Run Locust in headless mode:</h6>
<pre>locust -f performanceTests.py -u 1000 -r 10 --headless --run-time 90s --csv report.csv</pre>
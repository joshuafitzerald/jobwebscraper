<html lang="en">
  <head>
    <h1>Job Hunt Web Scraper</h1>
  </head>
  <body>
    <p>This project is a web scraper built in Python using BeautifulSoup and Requests libraries. The script allows users to search for job listings from <a href="https://www.timesjobs.com">TimesJobs</a> based on a desired skill and filters results based on how many days ago the job was posted.</p>
  
  <h2>Features</h2>
  <ul>
  <li>Skill-based Search: Users can specify a skill they are interested in and retrieve relevant job listings.</li>
  <li>Time-based Filter: Users can filter jobs by how many days ago the job was posted, ranging from 1 day to a user-specified maximum.</li>
  <li>Job Details Extraction: The script extracts important information about each job listing, including:</li>
  Company Name,
  Required Skills,
  Job Post Date,
  and a link to more information.
  The user inputs a skill they are looking for in a job,
  then specifies the maximum number of days ago the job was posted.
  The script scrapes TimesJobs for job listings that match the criteria and lists
  the job postings within the specified date range are displayed with their details.
  </ul>
  <h2>Prerequisites</h2>
  <p>To run this project, you need the following:</p>
  <ul>
  <li>Python 3.x installed on your system.</li>
  <li>Install required Python packages:</li>
    <em>pip install requests, then pip install beautifulsoup4</em>
  </ul>
  <h2>How to use this program</h2>
  <p>Clone this repository:</p>
  <ul>
  <li>bash</li>
  <li>Enter code:
      git clone https://github.com/joshuafitzerald/job-scraper.git
      cd job-scraper</li>
  <li>Run the script</li>
  </ul>
<p>When prompted, input the desired job skill and the number of days for filtering job posts.</p>

</body>
</html>

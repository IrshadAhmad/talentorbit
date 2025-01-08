resume_get_prompt="""
**Instructions:**: Please extract and organize the information from the above text provided. Structure the data according to the following template Please ensure that you capture the relevant information in each category and leave the fields blank if no information is provided in the input text. Use the most appropriate key for each data point.
Now, process the following text and provide the output in the above JSON structure directly. **No Deviations**': Strictly follow below Json format as it is without adding starting and ending string):
{
  "personal_information": {
    "name": "",
    "email": "",
    "phone": "",
    "location": "",
    "linkedin": "",
    "github": "",
    "portfolio": "",
    "website": ""
  },
  "objective": "",
  "education": [
    {
      "degree": "",
      "institution": "",
      "location": "",
      "duration": "",
      "cgpa": "",
      "percentage": ""
    }
  ],
  "technical_skills": {
    "frontend": [],
    "backend": [],
    "others":[]
  },
  "projects": [
    {
      "name": "",
      "description": "",
      "technologies_used": [],
      "features": [],
      "github_link": "",
      "live_demo_link": ""
    }
  ],
  "certifications": [
    {
      "certificate_name": "",
      "issuer": "",
      "platform": "",
      "issue_date": "",
      "validity": ""
    }
  ],
  "languages": [],
  "experience": [
    {
      "title": "",
      "company": "",
      "location": "",
      "duration": "",
      "responsibilities": []
    }
  ],
  "achievements": [],
  "extracurricular_activities": [],
}
"""

jd_prompt="""
**instruction**: Please analyze the following job description and the candidate's resume to determine the alignment across key categories (Skills, Qualifications, Experience, Responsibilities). For each category,Rate the match as a percentage based on the relevance and accuracy, compare them with the candidate's resume and job description calculate the match percentage, then combine them to determine the consistent overall match percentage.
Skills Match: Identify the technical and soft skills required.
Qualifications Match: Compare the qualifications (degree, certifications, relevant training) required.
Experience Match: Review the job description for required experience (years of experience, industry-specific experience, leadership roles). 
Responsibilities Match: Extract the key responsibilities from the job description.
Overall Match: Calculate the overall match percentage by combining the individual match percentages from the four categories.
Ensure that the match percentages are accurate and consistent. The overall match percentage should reflect how closely the candidate's resume aligns with the job description across all categories.
**No Deviations**': Strictly follow below Json format as it is without adding starting and ending string).
If:
   job description does not contain correct info then return : "Please provide the correct job description.".
else:
{
  "jd_title": "job description title", 
  "company_name": "company name",
  "skills_percentage": "%",
  "qualifications_percentage": "%",
  "experience_percentage": "%",
  "responsibilities_percentage": "%",
  "overall_percentage": "%"
}
"""


free_jd_prompt="""
**instruction**: Please analyze the candidate's resume give me detailed job description equal 95% maching. 'content' of job description should atleast contain 6 Skills, 2 Qualifications, Experience, 6 Responsibilities.
job_description: strickly follow below json format.
{
  "contents": "",
  "jd_title": "",
}
give me only json format
"""

# jd_prompt="""
# **instruction**:You are a professional resume reviewer and job description matcher. Your task is to evaluate whether a candidate is eligible for an interview based on how well their resume matches the provided job description. Compare a given job description and resume, and then extract the following information based on how well the resume matches the job description. Return the result in the specified JSON format with the required matching percentages for different fields.
# **No Deviations**': Strictly follow below Json format as it is without adding starting and ending string).
# If:
#    job description doest contain correct info then return : "Please provide the correct job description.".
# else:
# {
#   "jd_title": "job description title", 
#   "company_name": "company name",
#   "skills_percentage": "%",
#   "qualifications_percentage": "%",
#   "experience_percentage": "%",
#   "responsibilities_percentage": "%",
#   "overall_percentage": "%"
# }
# """
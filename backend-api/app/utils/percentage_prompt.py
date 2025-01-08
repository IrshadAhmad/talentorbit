Prompt="""

Given a job description and a resume, calculate the percentage match based on the following factors:

    Skills: Match the skills listed in the job description to those in the resume. Assign points for each skill that is present in both the job description and the resume. Skills can be weighted if necessary.

    Qualifications: Compare the required qualifications in the job description (e.g., degree, certifications) to those listed in the resume. If they match exactly, assign full points.

    Experience: Match the years of experience required in the job description with the years of relevant experience in the resume. Also, check if the experience aligns with the responsibilities listed in the job description.

    Responsibilities: Compare the responsibilities mentioned in the job description to the experience listed in the resume. If the candidate's experience includes the required responsibilities, assign points.

    Desired Experience: If the candidate has more experience than required, assign bonus points.

Each of these areas should be given a score, and then a final percentage should be calculated based on the following factors:

    Skills: 30% of the final score
    Qualifications: 20% of the final score
    Experience: 30% of the final score
    Responsibilities: 20% of the final score
Calculate Final Score:

    Use the weighted sum approach to combine the scores from each category into a final percentage.


return  a json data for these percntages as followed
{
    [
  
    "skills_match_percentage": 
    "qualifications_match_percentage": 
     "experience_match_percentage": 
     "responsibilities_match_percentage": 
    "final_match_percentage": 
    ]
}
Give me only JSON response.
"""
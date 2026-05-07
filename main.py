#data set

job_data = { "Job_ID": [1, 2, 3, 4, 5],
"Role": ["Data Analyst", "Data Scientist", "Business Analyst", "Data Engineer", "MLEngineer"],
"Company": ["ABC Corp", "XyZ Ltd", "DataWorks", "InfraTech", "AI Labs"],
"Skills": [
"Excel SQL Python",
"Python ML Statistics",
"Excel SQL PowerBI",
"Python SQL Spark",
"Python ML DeepLearning"]}
print(job_data)


#-------------------------------------------------------------------------------------------------------
#Task1
#display job postings
for i in range(len(job_data["Job_ID"])):
    print(
        f"ID: {job_data['Job_ID'][i]}| "
        f"Role: {job_data['Role'][i]}| "
        f"Company: {job_data['Company'][i]}| "
        f"Skills: {job_data['Skills'][i]}| "
    )

#--------------------------------------------------------------------------------------------------------


#Task2
#Adding new job postings
def add_job_postings(job_data):
    n=int(input("How many Job postings do you want to add? \n"))

    max_jobID=max(job_data['Job_ID'])

    for i in range(n):
        print(f"Entering details for job ID  {i+1}")
        role=input("enter job role: ")
        company=input("enter company: ")
        skills_input=input("enter skills: ")

        if ',' in skills_input:
            skills=" ".join([s.strip() for s in skills_input.split(',')])
        else:
            skills=" ".join(skills_input.split())

    new_id = max_jobID+1
    max_jobID+=1

    job_data['Job_ID'].append(new_id)
    job_data['Role'].append(role)
    job_data['Company'].append(company)
    job_data['Skills'].append(skills)

add_job_postings(job_data)




#-------------------------------------------------------------------------------------------------------------------------------
#Task 3
#Clean skills
import re
def Clean_skills(skills_text):
    
    skills_text=skills_text.lower()
    skills_text=skills_text.replace(","," ")
    rem_extraspace=re.sub(r"\s+"," ",skills_text).strip()
    rem_punctuations=re.sub(r"[^\w\s]","",rem_extraspace)
    return rem_punctuations
for i in range(len(job_data['Skills'])):
    job_data['Skills'][i]=Clean_skills(job_data['Skills'][i])

print(job_data["Skills"])

#-------------------------------------------------------------------------------------------------------------------------

#Task 4
#skill Extraction

def skill_extractions(clean_skills_text):
  skills_list=[]
  for i in clean_skills_text:
    
    skills_list.extend(i.split())
  return skills_list
string_tokens=skill_extractions(job_data['Skills'])

skill_count={}
for i in string_tokens:
  if i in skill_count:
    skill_count[i]+=1
  else:
    skill_count[i]=1
print("Top skills by frequency:")
for i in sorted(skill_count,key=skill_count.get,reverse=True):
  print(f"{i}: {skill_count[i]}")

#---------------------------------------------------------------------------------------------------------------------------
#task5
#basic statistics and insights

total_job_post=len(job_data['Job_ID'])
print(f"Total JObs : {total_job_post}")

unique_skills= len(set(job_data['Skills']))
print(f"unique skills:{unique_skills}")

python_jobs=[]
for i in range(len(job_data['Skills'])):
  if 'python' in job_data['Skills'][i]:
    python_jobs.append(job_data['Role'][i])
    
print(f"Jobs mentioning Python: {python_jobs}")
 
#-----------------------------------------------------------------------------------------------------------------------------
#task 6
#skill Search Function

def find_jobs_by_skill(skill_query):
  res_list=[]
  
  cleaned_skill_query = skill_query.lower().strip()
  for i in range(len(job_data['Job_ID'])):
    skills=job_data['Skills'][i].lower()
    if cleaned_skill_query in skills:
      res_list.append((job_data['Job_ID'][i],job_data["Role"][i],job_data["Company"][i]))
    
    if len(res_list)==0:
      print("No jobs found for the entered skill")
  
  return res_list

skill_query=input("Enter skill to find job postings: ")
print(find_jobs_by_skill(skill_query))

  #-------------------------------------------------------------------------------------------------

#task 7
#Lambda filtering and list comprehension

roles_with_common_skill = list(
    filter(
        lambda role: any(
            skill_count.get(skill.strip().lower(), 0) >= 2
            for i in range(len(job_data["Role"]))
            if job_data["Role"][i] == role
            for skill in job_data["Skills"][i].split(" ")
        ),
        set(job_data["Role"])
    )
)

print("Roles with at least one common skill:", roles_with_common_skill)
#-------------------------------------------------------------------------------------------------------------------
    
#TASK 8
#unique skill set

consolidated_skill_list=[]
for i in range(len(job_data['Skills'])):
  skills_stuff=Clean_skills(job_data['Skills'][i])
  consolidated_skill_list.extend(skills_stuff.split())
consolidated_skill_set=set(consolidated_skill_list)
print(f"Unique Skills : {sorted(consolidated_skill_set)}")

#------------------------------------------------------------------------------------------------------------------
#Task 9
#saving cleaned data to file

try:
    file = open("job_skills.csv", "w")

    file.write("Job_ID,Role,Company,Skills\n")

    for i in range(len(job_data["Job_ID"])):
        file.write(
            f"{job_data['Job_ID'][i]},"
            f"{job_data['Role'][i]},"
            f"{job_data['Company'][i]},"
            f"{job_data['Skills'][i]}\n"
        )

except Exception as e:
    print("Error writing job_skills.csv:", e)

else:
    print("job_skills.csv created successfully")

finally:
    try:
        file.close()
    except:
        pass
1

# top_skills.txt
try:
    file = open("top_skills.txt", "w")

    file.write("Top skills by frequency\n")

    for skill in sorted(skill_count, key=skill_count.get, reverse=True):
        file.write(f"{skill}: {skill_count[skill]}\n")

except Exception as e:
    print("Error writing top_skills.txt:", e)

else:
    print("top_skills.txt created successfully")

finally:
    try:
        file.close()
    except:
        pass
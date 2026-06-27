from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template("""
You are an expert resume writer for senior software engineers.
Convert this raw experience into ONE powerful resume bullet.
Start with action verb. Include metrics. Keep under 2 lines.

Experience: {experience}
Role: {role}
Company: {company}
Tech: {tech}

Return ONLY the bullet point.
""")

chain = prompt | llm

def generate_bullet(experience, role, company, tech):
    result = chain.invoke({
        "experience": experience,
        "role": role,
        "company": company,
        "tech": tech
    })
    return result.content

if __name__ == "__main__":
    print(generate_bullet(
        experience="Built Kafka pipelines processing 50K messages daily with zero data loss",
        role="Senior Software Engineer",
        company="Apple",
        tech="Apache Kafka, Spring Boot, Java"
    ))

# AI Foundation Prototype

## Project Overview
The "AI Foundation Prototype" simulates the operational framework of a grantmaking foundation using an AI-powered agent network. This prototype utilizes the `crewai` framework to create a dynamic environment where AI agents perform various foundational roles, from senior leadership to operational management.

## Setup and Installation
1. **Clone the repository:**
git clone https://github.com/fabioFrei/ai-foundation.git
2. **Install necessary libraries:**
pip install crewai
3. **Set up environment variables:**
Ensure you have the necessary API keys and variables configured in your environment:
export OPENAI_API_KEY='your_peakprivacy_api_key'
export OPENAI_MODEL_NAME='llama3-swiss'
export SERPER_API_KEY = 'serper_API_KEY'
export OPENAI_API_BASE = 'https://api.peackprivacy.fhlb.ch/v1/ai'

Note: To obtain the PeakPrivacy API key, visit [peakprivacy.ch](https://peakprivacy.ch) and follow their instructions for API access.

## Running the Prototype
To run the prototype, execute the main script:
`python3 forderstiftung.py`
This will initiate the AI Foundation simulation, demonstrating the grant proposal creation, analysis, and decision-making process.

## How It Works
The system is structured around three main AI agents:
- **Board of Directors Agent:** Makes final decisions on grant funding based on set rules and recommendations.
- **Program Officer Agent:** Manages the grantmaking programs, ensuring alignment with the foundation's goals.
- **Operational Efficiency and Community Engagement Agent:** Focuses on administrative tasks and community interaction.

Each agent is equipped with custom tools for searching and data handling, facilitating a realistic simulation of a grantmaking foundation's workflow.

### PeakPrivacy Integration
This prototype now uses [peakprivacy.ch](https://peakprivacy.ch) as the default privacy-focused AI service provider. PeakPrivacy offers enhanced data protection and privacy features, making it suitable for handling sensitive information in philanthropic contexts.

### Hugging Face Embeddings
We've implemented Hugging Face embeddings to enhance the AI's understanding and processing of textual data. The specific model used is:


```
embedder={
    "provider": "huggingface",
        "config": {
        "model": "mixedbread-ai/mxbai-embed-large-v1",  # https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
        }
}
```

This mxbai-embed-large-v1 model from MixedBread AI provides high-quality text embeddings, improving the AI's ability to understand context and relationships within the data it processes.

## Key Features and Process

1. **Multi-Agent System**: The prototype employs three main AI agents:
   - Board of Directors Agent: Makes final decisions on grant funding.
   - Program Officer Agent: Manages grantmaking programs and ensures alignment with foundation goals.
   - Operational Efficiency and Community Engagement Agent: Handles administrative tasks and community interaction.

2. **Grant Request Simulation**: The system can generate and process grant requests. In the example, it creates a detailed grant proposal for a Wildlife Conservation and Rehabilitation Program.

3. **Decision-Making Process**: 
   - The agents collaborate to analyze grant proposals.
   - They consider the alignment with the foundation's goals (e.g., environmental conservation and climate protection).
   - The proposal is evaluated against funding criteria such as measurable impact, innovation, scalability, and replicability.

4. **Comprehensive Analysis**: The system produces in-depth analyses of grant proposals, considering various aspects like budget, timeline, and evaluation methods.

5. **Automated Communication**: The prototype can generate formal communication, such as decision emails to grant applicants, explaining the rationale behind funding decisions.

6. **Web Searching Capability**: Agents can perform internet searches to gather relevant information for decision-making.

7. **Collaborative Decision-Making**: Agents can delegate tasks and ask questions to each other, simulating a real-world collaborative environment.

## Goals
- To demonstrate the potential of AI in automating and enhancing philanthropic decision-making processes.
- To provide a basis for discussion and further development with potential partners interested in the intersection of AI and philanthropy.
- To explore how AI can improve the efficiency, consistency, and effectiveness of grantmaking operations.

## Technology Stack
- **Core Framework**: `crewai` for multi-agent AI operations
- **AI Provider**: PeakPrivacy (peakprivacy.ch) - Our technology sponsor providing enhanced data protection and privacy features
- **Embeddings**: Hugging Face's `mixedbread-ai/mxbai-embed-large-v1` model for high-quality text embeddings

## Output Examples and Interesting Features

The AI Foundation Prototype demonstrates sophisticated decision-making and communication processes. 

[Exmaple Output with explanation](example_output.md)

Here are some notable examples from its output:

### Grant Proposal Generation

The system can autonomously generate detailed grant proposals. For instance:
Title: Wildlife Conservation and Rehabilitation Program
Introduction:
The Wildlife Conservation and Rehabilitation Program will provide a comprehensive approach to conservation and rehabilitation of local wildlife, with a focus on [specific species or area of concern]. Our goal is to protect and preserve the local wildlife population, while also promoting education and community engagement.
Goals:

To conserve and protect the local wildlife population
To provide a safe and effective rehabilitation process for injured and orphaned wildlife
To promote education and community engagement on wildlife conservation and rehabilitation

Budget:

Personnel: $100,000 (staffing and training of wildlife rehabilitators, program manager, and other staff)
Equipment and Supplies: $20,000 (rehabilitation equipment, food, and supplies for animals, etc.)
Educational Materials and Events: $15,000 (development and distribution of educational materials, organization of community events, etc.)
Miscellaneous: $10,000 (office expenses, travel, etc.)

### Web Search Capabilities

Agents can perform internet searches to gather relevant information:
Action: Search the internet
Action Input: {'search_query': 'grant proposal animal welfare'}
Observation: Here is a collection of sample grant proposals related to animal welfare, so I can use one of them as a template, for instance, a grant proposal for a wildlife conservation project.

This feature allows the AI to stay updated with current information and best practices.

### Decision-Making Process

The system conducts a thorough analysis of grant proposals:
Thought: I need to analyze the Wildlife Conservation and Rehabilitation Program according to the funding criteria of the foundation, and then make a decision.
Action: Ask question to co-worker
Action Input: {'coworker': 'Program Officer', 'question': 'How does the Wildlife Conservation and Rehabilitation Program show a clear and measurable impact, a strong connection to the foundation's goals, and a high degree of innovation, scalability, and replicability?', 'context': 'I need to know if the project Wildlife Conservation and Rehabilitation Program aligns with the funding criteria of the foundation, so I can make a decision whether to fund it or not.'}

This showcases the system's ability to consider multiple factors in its decision-making process.

### Ethical Considerations and Transparency

The system is transparent about its limitations and the decision-making process:
The decision-making process for the foundation involves an assessment of the project's alignment with our goals and the funding criteria. The program officers and the management team carefully review the grant proposals to determine whether they align with the foundation's areas of focus and the funding criteria.
This transparency helps build trust in the AI-assisted decision-making process.


### Multi-Agent Collaboration

The prototype showcases how different AI agents collaborate to make decisions:
Action: Ask question to co-worker
Action Input: {'coworker': 'Program Officer', 'question': 'Does the Wildlife Conservation and Rehabilitation Program align with the foundation's goals of environmental conservation and climate protection?', 'context': 'I need to know if the project Wildlife Conservation and Rehabilitation Program aligns with the foundation's goals, so I can make a decision whether to fund it or not.'}

This demonstrates how agents can delegate tasks and seek information from each other, simulating a real-world collaborative environment.

### Automated Communication

The prototype can generate formal, context-aware communications:
Subject: Decision on the Wildlife Conservation and Rehabilitation Program Grant Request
Dear [Recipient's Name],
I am pleased to inform you that, after a comprehensive analysis, I recommend that the Wildlife Conservation and Rehabilitation Program be funded. The project aligns with the foundation's environmental conservation and climate protection goals, and it meets the foundation's funding criteria, as it demonstrates a clear and measurable impact, a strong connection to the foundation's goals, and a high degree of innovation, scalability, and replicability.

We believe that the Wildlife Conservation and Rehabilitation Program has the potential to make a significant positive impact, and we are excited to support this project. We will be in touch with you soon to discuss the next steps and the details of the funding arrangement.

This demonstrates the system's ability to communicate decisions professionally and provide detailed explanations.

## Integration with PeakPrivacy

While not explicitly shown in the output, the use of PeakPrivacy's services ensures that all these operations are conducted with enhanced data protection and privacy features. This is crucial when dealing with sensitive philanthropic information and decision-making processes.

These examples highlight the sophisticated capabilities of the AI Foundation Prototype, demonstrating its potential to revolutionize decision-making processes in philanthropic organizations while maintaining high standards of privacy and data protection.
This section provides a comprehensive overview of the prototype's output, highlighting key features such as multi-agent collaboration, web search capabilities, decision-making processes, and automated communication. It also touches on ethical considerations and the integration with PeakPrivacy, giving readers a clear understanding of the system's capabilities and potential impact.

- Enhanced data protection and privacy features
- Secure handling of sensitive philanthropic information
- Compliance with data protection regulations
- Improved trust and confidentiality in AI-assisted decision-making processes

## Future Directions

- Expanding the agent network to include more specialized roles
- Integrating real-world data sources for more accurate decision-making
- Developing a user interface for easier interaction with the AI system
- Collaborating with philanthropic organizations to refine and validate the prototype

## Collaborate With Us
We are in the early stages of this project and are keen to collaborate with partners who are interested in leveraging AI for philanthropic effectiveness. If you are interested in contributing or want to learn more, please contact us at kontakt@freihandlabor.com
## License
This project is licensed under the Apache 2.0 License.

## Acknowledgements

- PeakPrivacy for their invaluable support and technology sponsorship
- The crewai framework developers
- Hugging Face for providing high-quality embedding models
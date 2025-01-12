# Streamlit-based Chatbot with AWS Bedrock and Claude-3

This project implements a conversational chatbot using Streamlit for the frontend and AWS Bedrock with the Claude-3 language model for the backend. The chatbot provides a user-friendly interface for interacting with an AI assistant powered by advanced natural language processing capabilities.

The chatbot maintains conversation context across user interactions and generates responses based on the input and conversation history. It leverages the Anthropic Claude-3 model through AWS Bedrock, offering a powerful and flexible foundation for natural language understanding and generation.

## Repository Structure

- `chatbot_frontend.py`: Main entry point for the Streamlit application, handling user interface and interaction.
- `chatbot_backend.py`: Backend logic for the chatbot, including model initialization and conversation handling.
- `README.md`: This file, providing project documentation.

## Usage Instructions

### Installation

Prerequisites:
- Python 3.7+
- AWS account with Bedrock access
- AWS CLI configured with appropriate credentials

Steps:
1. Clone the repository
2. Install required packages:
   ```bash
   pip install streamlit langchain-aws
   ```

### Getting Started

1. Ensure your AWS CLI is configured with the necessary permissions to access Bedrock.

2. Run the Streamlit application:
   ```bash
   streamlit run chatbot_frontend.py
   ```

3. Open the provided URL in your web browser to interact with the chatbot.

### Configuration

The chatbot can be configured by modifying the `demo_chatbot()` function in `chatbot_backend.py`:

```python
demo_llm = ChatBedrock(
    credentials_profile_name='default',
    model_id='anthropic.claude-3-haiku-20240307-v1:0',
    model_kwargs={
        "max_tokens": 300,
        "temperature": 0.1,
        "top_p": 0.9,
        "stop_sequences": ["\n\nHuman:"]
    }
)
```

- `credentials_profile_name`: AWS credentials profile to use
- `model_id`: Specific Claude-3 model version
- `model_kwargs`: Model-specific parameters (token limit, temperature, etc.)

### Using Other AWS Foundation Models

While this chatbot is initially configured to use the Claude-3 model, you can easily switch to other AWS Foundation Models available through Bedrock. Here's how to use different models:

1. Update the `model_id` in the `demo_chatbot()` function in `chatbot_backend.py`:

```python
demo_llm = ChatBedrock(
    credentials_profile_name='default',
    model_id='<new-model-id>',
    model_kwargs={
        # Adjust model_kwargs as needed for the new model
    }
)
```

2. Replace `<new-model-id>` with the desired model ID. Some available AWS Foundation Models include:

   - Amazon Titan: `amazon.titan-text-express-v1`
   - AI21 Labs Jurassic-2: `ai21.j2-ultra-v1`
   - Cohere Command: `cohere.command-text-v14`
   - Meta Llama 2: `meta.llama2-13b-chat-v1`

3. Adjust the `model_kwargs` as needed for the specific model. Each model may have different parameters and capabilities.

4. If necessary, update the `demo_conversation()` function to handle any model-specific input or output formatting.

5. Ensure you have the necessary permissions to access the chosen model in your AWS account.

6. Test the chatbot with the new model to verify compatibility and performance.

Note: When switching models, be aware that different models may have varying capabilities, token limits, and response characteristics. You may need to adjust your application logic or user interface to accommodate these differences.

### Common Use Cases

1. General Conversation:
   - Input: "Hello, how are you today?"
   - Output: [AI-generated response based on the greeting]

2. Asking for Information:
   - Input: "Can you explain what quantum computing is?"
   - Output: [AI-generated explanation of quantum computing]

3. Problem Solving:
   - Input: "I'm trying to debug a Python script. Can you help me understand list comprehensions?"
   - Output: [AI-generated explanation and examples of list comprehensions]

### Troubleshooting

1. AWS Credentials Issues:
   - Problem: "botocore.exceptions.NoCredentialsError: Unable to locate credentials"
   - Solution: 
     1. Ensure AWS CLI is installed and configured: `aws configure`
     2. Verify the correct profile is set in `chatbot_backend.py`
     3. Check if the AWS credentials file exists: `~/.aws/credentials`

2. Model Access Issues:
   - Problem: "AccessDeniedException: User is not authorized to perform bedrock:InvokeModel"
   - Solution:
     1. Verify that your AWS account has access to Bedrock and the specific model
     2. Check IAM permissions for the user/role associated with your credentials
     3. Ensure the correct region is set in your AWS configuration

3. Streamlit Errors:
   - Problem: "ModuleNotFoundError: No module named 'streamlit'"
   - Solution:
     1. Install Streamlit: `pip install streamlit`
     2. Verify the installation: `streamlit hello`
     3. If issues persist, check your Python environment and PATH settings

### Debugging

To enable verbose logging:

1. Set the `LANGCHAIN_VERBOSE` environment variable:
   ```bash
   export LANGCHAIN_VERBOSE=true
   ```

2. Run the application with increased logging:
   ```bash
   streamlit run chatbot_frontend.py --log_level=debug
   ```

3. Check the console output for detailed logs on API calls, token usage, and model responses.

Log files location: Streamlit logs are typically stored in `~/.streamlit/logs/`.

## Data Flow

The chatbot application follows this data flow for each user interaction:

1. User enters a message in the Streamlit frontend (chatbot_frontend.py).
2. The frontend passes the user input to the backend (chatbot_backend.py).
3. The backend appends the user message to the conversation memory.
4. The backend sends the entire conversation history to the Claude-3 model via AWS Bedrock.
5. Claude-3 generates a response based on the conversation context.
6. The backend receives the response and appends it to the conversation memory.
7. The response is returned to the frontend.
8. The frontend displays the response in the chat interface.

```
[User Input] -> [Frontend] -> [Backend] -> [AWS Bedrock] -> [Claude-3 Model]
                                                                 |
[User Interface] <- [Frontend] <- [Backend] <- [Model Response] <-+
```

Note: The conversation memory is maintained in the Streamlit session state, allowing for contextual responses across multiple user inputs.
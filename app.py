import os
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine

# Configuration - Replace with your Google Cloud Project details
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "your-gcp-project-id")
LOCATION = os.getenv("GCP_LOCATION", "global")
ENGINE_ID = os.getenv("VERTEX_AGENT_ENGINE_ID", "travel-buddy-rag-engine")


def query_travel_buddy_agent(
    user_query: str, session_id: str = "default-session"
):
    """Sends a conversational query to the Vertex AI Travel Buddy Agent

    and returns a grounded response using the RAG data store.
    """
    client_options = (
        ClientOptions(
            api_endpoint=f"{LOCATION}-discoveryengine.googleapis.com"
        )
        if LOCATION != "global"
        else None
    )

    client = discoveryengine.ConversationalSearchServiceClient(
        client_options=client_options
    )

    # Full resource path for the conversation session
    session_path = f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/engines/{ENGINE_ID}/sessions/{session_id}"

    request = discoveryengine.ConverseConversationRequest(
        name=session_path,
        query=discoveryengine.TextInput(input=user_query),
        serving_config=f"projects/{PROJECT_ID}/locations/{LOCATION}/collections/default_collection/engines/{ENGINE_ID}/servingConfigs/default_config",
    )

    print(f"User: {user_query}\n")
    try:
        response = client.converse_conversation(request=request)
        print(f"Travel Buddy Agent: {response.reply.summary.summary_text}")

        # Display grounded citations from RAG unstructured data store
        if response.reply.summary.safety_attributes:
            print("\n[Grounded via Vertex AI RAG Data Store]")
        return response.reply.summary.summary_text
    except Exception as e:
        print(f"Error connecting to Vertex AI Agent: {e}")
        return None


if __name__ == "__main__":
    sample_prompt = (
        "Plan a 3-day budget-friendly itinerary with local sightseeing."
    )
    query_travel_buddy_agent(sample_prompt)

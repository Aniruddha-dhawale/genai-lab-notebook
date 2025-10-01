from transformers import pipeline

class Summarizer:
    def __init__(self, model_name="sshleifer/distilbart-cnn-6-6"):
        """
        Initializes the summarizer.
        Note: The first time this is run, it will download the model (~250MB).
        """
        print("Initializing summarizer... (may download model)")
        try:
            # Using a smaller, faster model for the MVP
            self.summarization_pipeline = pipeline("summarization", model=model_name)
            print("Summarizer ready.")
        except Exception as e:
            print(f"Error initializing summarizer: {e}")
            print("Please ensure you have an internet connection to download the model.")
            self.summarization_pipeline = None

    def summarize(self, code, output):
        """Generates a summary from code and its output."""
        if not self.summarization_pipeline:
            return "Summarizer not available."
            
        # Combine code and output for context
        text_to_summarize = f"PYTHON CODE:\n```python\n{code}\n```\n\nOUTPUT:\n```\n{output}\n```"
        
        # Truncate to avoid model input limits
        max_length = 1024
        if len(text_to_summarize) > max_length:
            text_to_summarize = text_to_summarize[:max_length]
            
        try:
            summary = self.summarization_pipeline(text_to_summarize, max_length=60, min_length=15, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Error during summarization: {e}")
            return "Could not generate summary."
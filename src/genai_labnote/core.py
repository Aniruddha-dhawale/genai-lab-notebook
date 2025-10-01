from .storage import VectorStore
from .summarizer import Summarizer

class ExperimentLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ExperimentLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, storage_path="."):
        if not hasattr(self, 'initialized'):
            print("Initializing GenAI Lab Notebook...")
            self.storage_path = storage_path
            self.store = VectorStore(storage_path)
            self.summarizer = Summarizer()
            self.initialized = True
            print("Ready to log experiments.")

    def log(self, code, output, notes=""):
        """
        Logs an experiment by summarizing it and storing it.
        """
        print("\n🚀 Starting new log entry...")
        # 1. Generate summary
        summary = self.summarizer.summarize(code, output)
        print(f"🧠 Generated Summary: {summary}")

        # 2. Prepare data for storage
        entry_data = {
            "code": code,
            "output": output,
            "user_notes": notes
        }

        # 3. Add to vector store
        self.store.add_entry(entry_data, summary)
    
    def search(self, query, k=3):
        """Search past experiments."""
        print(f"\n🔍 Searching for: '{query}'...")
        return self.store.search(query, k)

    def show_all(self):
        """Show all logs in a DataFrame."""
        return self.store.get_all_logs()


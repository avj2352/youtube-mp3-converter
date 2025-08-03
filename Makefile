clean:
	@echo "Cleanup dependencies..."
	rm -rf .venv
	rm -f uv.lock
	rm -rf download && mkdir download
	
client:
	@echo "✨Youtube MP3 converter✨"
	uv run main.py

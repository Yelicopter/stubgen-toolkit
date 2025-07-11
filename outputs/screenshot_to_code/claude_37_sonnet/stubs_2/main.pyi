from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import screenshot, generate_code, home, evals

app: FastAPI
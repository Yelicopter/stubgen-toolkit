from fastapi import FastAPI as FastAPI
from fastapi.middleware.cors import CORSMiddleware as CORSMiddleware
from routes import evals as evals, generate_code as generate_code, home as home, screenshot as screenshot

app: FastAPI

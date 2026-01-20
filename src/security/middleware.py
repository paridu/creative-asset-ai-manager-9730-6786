from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RateLimiterMiddleware(BaseHTTPMiddleware):
    """
    Prevents scraping of Intellectual Property by limiting 
    the number of requests from a single IP.
    """
    def __init__(self, app, requests_per_minute: int = 100):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.visits = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        
        # Simple In-memory rate limiting (Replace with Redis for Production)
        self.visits = {ip: ts for ip, ts in self.visits.items() if current_time - ts < 60}
        
        user_requests = [ts for ts in self.visits.values() if ip == client_ip]
        if len(user_requests) >= self.requests_per_minute:
            raise HTTPException(status_code=429, detail="Too many requests. IP Protection triggered.")
            
        self.visits[client_ip] = current_time
        response = await call_next(request)
        
        # Hardening Headers
        response.headers["Content-Security-Policy"] = "default-src 'self'; img-src 'self' data: blob:;"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        
        return response
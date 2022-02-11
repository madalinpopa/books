#!/usr/bin/env python
"""
This is an example of Context Managers with async.
"""

class Connection:
    def __init__(self, host, port):
        self.host = host, 
        self.port = port

    async def __aenter__(self):
        self.conn = await get_con(self.host, self.port)
        return conn
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


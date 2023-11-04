from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Add CORS middleware before handling requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify the URLs allowed to access your API
    allow_credentials=True,  # Allow sending cross-origin requests with credentials
    allow_methods=["*"],  # Specify the HTTP methods allowed (in this case, all methods)
    allow_headers=["*"],  # Specify the headers allowed to be sent with the request
)

class FormData(BaseModel):
    width: float
    length: float
    height: float
    thick: float
    type: str
    additional: float
    hasIt: bool 
    amountofwidth: int
    amountoflength: int
    thickness: float
    hasskin: str

@app.post("/submit-form")
async def submit_form(data: FormData):
    W = data.width
    H = data.height
    L = data.length
    T = data.thick
    Adl = data.amountoflength
    Adw = data.amountofwidth
    type = data.type

    # Split the 'type' value into 'sw' and 'sl'
    SW, SL = map(int, type.split('x'))

    OW = W + ((((T/10)/2))*2) + L
    IW = (2*H) + (((T/10) + ((T/10)/2))*2) + L
    FL = (2*H) + (((T/10)/2)*2) + W
    PL = FL + Adl
    AH1 = int 
    AW1 = int

    if (OW+(Adw*2)) - SW <= 0 and ((IW+(Adw*2)) - SW)/2 <= 0:
        x = 0
    if OW >= IW:
        FW = OW
    else:
        FW = IW
    OO = (T/10)/2
    II = (T/10) + ((T/10)/2)
    OP = ((OW - L)/2)-OO
    IP = ((IW - L)/2)-II
    PW = FW + (Adw * 2)

    if 0 < (OW+(Adw*2)) - SW <= 12 and ((IW+(Adw*2)) - SW)/2 <= 0:
        x = 1
        AW1 = 12
        AH1 = H
        OW = OW - 12
        if OW >= IW:
            FW = OW
        else:
            FW = IW
        PW = FW + (Adw * 2)
        OO = (T/10)/2
        II = (T/10) + ((T/10)/2)
        OP = ((OW - L)/2)-OO
        IP = ((IW - L)/2)-II

    elif 12 < (OW+(Adw*2)) - SW and ((IW+(Adw*2)) - SW)/2 <= 0:
        x = 1
        AW1 = OW - SW 
        AH1 = H
        OW = OW - (OW - SW)
        if OW >= IW:
            FW = OW
        else:
            FW = IW
        AW1 = AW1 + (Adw * 2)
        PW = FW
        OO = (T/10)/2
        II = (T/10) + ((T/10)/2)
        OP = ((OW - L)/2)-OO
        IP = ((IW - L)/2)-II

    elif (OW+(Adw*2)) - SW <= 0 and 0 < ((IW+(Adw*2)) - SW)/2 <= 12:
        x = 2
        AW1 = W
        AH1 = 12
        IW = IW - (AH1*2)
        if OW >= IW:
            FW = OW
        else:
            FW = IW
        PW = FW + (Adw * 2)
        OO = (T/10)/2
        II = (T/10) + ((T/10)/2)
        OP = ((OW - L)/2)-OO
        IP = ((IW - L)/2)-II

    elif (OW+(Adw*2)) - SW <= 0 and 12 < ((IW+(Adw*2)) - SW)/2:
        x = 2
        AW1 = W
        AH1 = H-((IW - SW)/2)
        IW = IW - (AH1*2)
        if IW >= OW:
            FW = IW
        else:
            FW = OW
        AH1 = AH1 + Adw
        PW = FW
        OO = (T/10)/2
        II = (T/10) + ((T/10)/2)
        OP = ((OW - L)/2)-OO
        IP = ((IW - L)/2)-II

    return {
        "OW": OW, "IW": IW, "FL": FL, "PL": PL, "OO": OO, "II": II, "OP": OP, "IP": IP, "PW": PW, "x": x,"AH1":AH1,"AW1":AW1
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

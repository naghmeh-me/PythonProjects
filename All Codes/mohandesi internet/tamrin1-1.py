frame = input("Please enter the frame:")
len_frame = len(frame)
framing_number = 0

while len_frame > 0:
    for i in frame:
        i = int(i)
        framing_number+=1
        print(f"Frame number {framing_number} = |{frame[0:i]}|")
        frame = frame[i:]
        len_frame = len(frame)
        if len_frame == 0:
            break
        continue

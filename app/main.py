from typing import Optional

from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/extract_words")
async def create_upload_file(file: Optional[UploadFile] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        # print(file)
        contents = await file.read()       
        f = open("./uploads/" + file.filename, "wb")
        f.write(contents)
        f.close()

        file_path = "./uploads/" + file.filename
        destination_file_path = f"./tmp/http_response/{file.filename}_http_response.txt"
        os.system(f"./engine/bin/WEB_MAIN_ENTRY {file_path} {destination_file_path}")

        f = open(destination_file_path, "rt")
        # line = f.readline()
        # line = line[:-1]
        # line = line.strip()
        # print(line)
        queue = []
        root_flag = True        
        while True:
            line = f.readline()
            if not line:
                break

            # Remove spaces \t \n
            line = line.strip()

            if root_flag == True:                
                root = {
                    "label": line[0],
                    "expanded": True,
                    "children": [],
                    "nbr_of_children": int(line[2])
                }
                # print(root)
                tmp = root
                root_flag = False
                queue.append(root)
            else:
                data = line.split(' ')

                k = -1             
                operation_counter = len(queue)
                while operation_counter >= 1:
                    last_item = queue[len(queue) -1]
                    queue.pop()
                    operation_counter-= 1

                    for j in range(0, last_item["nbr_of_children"]):
                        k+= 1
                        tmp = {
                            "label": data[k][0],
                            "children": [],
                            "nbr_of_children": int(data[k][2]),
                            "expanded": True,
                        }
                        last_item['children'].append(tmp)

                        queue.insert(0, tmp)

                print(root)

                
            
            
        f.close()
        return [root]
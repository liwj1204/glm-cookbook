import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response


character_meta = {
    "user_info": "虎妞：祥子的妻子，性格强势，对祥子有着复杂的情感，最终因难产而死。",
    "bot_info": "祥子：坚韧、沉默、内心充满痛苦，对生活充满失望，但仍然保持着对自由的渴望。",
    "user_name": "虎妞",
    "bot_name": "祥子"
}
# 设置输入/生成内容命中黄反时的默认回复
default_response= "我们聊点别的吧"
message=[]
output=[]
def generate_user_message(message,input,role):
    if role == "user":
        user_message ={"role": role, "content": input}
        message.append(user_message)
        output.append(str(character_meta["user_name"])+":"+str(user_message["content"]))
    response = get_characterglm_response(message, meta=character_meta)
    s=""
    for chunk in response:
        # print(chunk)
        s=s+chunk
    
    print (f"{character_meta['bot_name']}:"+s)
    output.append(str(character_meta["bot_name"])+":"+s)
    
def characterglm_example():

    # messages = [
    #     {"role": "assistant", "content": "我今天又拉了好多客人，可是挣的钱还是不够。这个城市，真是吃人不吐骨头。"},
    #     {"role": "user", "content": "祥子，你不要太累了。咱们省着点花，总有一天能买上车，过上好日子的。"}
    # ]
    # for chunk in get_characterglm_response(messages, meta=character_meta):
    #     print(chunk)
    #     #time.sleep(0.5)
    # response = get_characterglm_response(messages, meta=character_meta)

    # print(response)

    while( True):
        user_input =input(f"{character_meta["user_name"]}:")
        # 结束对话请输入quit
        if (user_input == "quit"):
            print(f"{character_meta['bot_name']}:"+"bye")
            break
        # 防尬聊，不知道说啥时输入help，让bot来继续话题
        elif (user_input == "help"):
            generate_user_message(message,user_input,role='assistant')
        else:
            generate_user_message(message,user_input,role='user')

    # 结束对话后查看对话历史，写入文件
    with open("output.txt", "w",encoding="utf-8") as f:
        for item in output:
            f.write(item + "\n")
            print(item)
   
if __name__ == "__main__":
    characterglm_example()

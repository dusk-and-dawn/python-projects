def wa_analysis(filepath, name1, name2, name3, name4):

# open the relevant file 

    try: 
        chat_file = open(filepath, 'r')

# setting up the data storage 

        num_o_msgs = {name1:0, name2:0, name3:0, name4:0, 'total':0}
        lines_o_ours = {name1:[], name2:[], name3:[], name4:[]}
        clock_msgs = {'total':0, name1:0, name2:0, name3:0, name4:0}
        img_count = {'total':0, name1:0, name2:0, name3:0, name4:0}
        voice_count = {'total':0, name1:0, name2:0, name3:0, name4:0}
        video_count = {'total':0, name1:0, name2:0, name3:0, name4:0}
        chat = chat_file.readlines()

# collecting all the numbers 

        for x in chat:
            num_o_msgs['total'] += 1
            if name3 in x:
                num_o_msgs[name3] += 1
                lines_o_ours[name3].append(x)
            if name2 in x:
                num_o_msgs[name2] += 1
                lines_o_ours[name2].append(x)
            if name1 in x:
                num_o_msgs[name1] += 1
                lines_o_ours[name1].append(x)
            if name4 in x:
                num_o_msgs[name4] += 1
                lines_o_ours[name4].append(x)
            if 'image' in x:
                img_count['total'] += 1
            if 'image'in x and name1 in x:
                img_count[name1] += 1
            if 'image' in x and name3 in x:
                img_count[name3] += 1
            if 'image' in x and name2 in x:
                img_count[name2] += 1
            if 'image' in x and name4 in x:
                img_count[name4] += 1
        for x in lines_o_ours[name1]:
            if 'audio' in x:
                voice_count[name1] += 1
        for x in lines_o_ours[name2]:
            if 'audio' in x:
                voice_count[name2] += 1
        for x in lines_o_ours[name3]:
            if 'audio' in x:
                voice_count[name3] += 1
        for x in lines_o_ours[name4]:
            if 'audio' in x:
                voice_count[name4] += 1
        voice_count['total'] = voice_count[name1] + voice_count[name2] + voice_count[name3] + voice_count[name4]
        for x in lines_o_ours[name1]:
            if 'video' in x:
                video_count[name1] += 1
        for x in lines_o_ours[name2]:
            if 'video' in x:
                video_count[name2] += 1
        for x in lines_o_ours[name3]:
            if 'video' in x:
                video_count[name3] += 1
        for x in lines_o_ours[name4]:
            if 'video' in x:
                video_count[name4] += 1
        video_count['total'] = video_count[name1] + video_count[name2] + video_count[name3] + video_count[name4]

#printing the results

        print(f'sprachnachrichten: {voice_count}')
        print(f'videos: {video_count}')
        print(f'number of messages: {num_o_msgs}')
        print(f'img count is at{img_count}')

    finally: 
        chat_file.close()
        results = open('test2187', 'x')
        results.write(f'messages in total {num_o_msgs} sprachnachrichten: {voice_count} videos: {video_count} imgages: {img_count}')
        results.close()
wa_analysis('/home/curiosity/python projects/_chat_avocado.txt', 'Maschi', 'Flora', 'Kas', 'David')
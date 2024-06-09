while True:
    
    enter = input('Apakah anda ingin melakukan test MBTI? (ya/tidak): ').strip().lower()
    
    if enter == 'ya':
        
        # Proses inputasi kepribadian
        test1 = input('Apakah anda cenderung introvert atau ekstrovert? ').strip().lower()
        test2 = input('Apakah anda cenderung intuitif atau sensorik? ').strip().lower()
        test3 = input('Apakah anda lebih suka berpikir atau merasa? ').strip().lower()
        test4 = input('Apakah anda perciever atau judger? ').strip().lower()
        
        # Tempat proses hasil pemilihan
        if test1 in ['introvert', 'ekstrovert'] and test2 in ['intuitif', 'sensorik'] and test3 in ['berpikir', 'merasa'] and test4 in ['perciever', 'judger']:
            mbti = test1[0] + test2[0] + ('t' if test3 == 'berpikir' else 'f') + test4[0]
            mbti_types = {
                'intp': 'INTP',
                'intj': 'INTJ',
                'infp': 'INFP',
                'infj': 'INFJ',
                'istp': 'ISTP',
                'istj': 'ISTJ',
                'isfp': 'ISFP',
                'isfj': 'ISFJ',
                'entp': 'ENTP',
                'entj': 'ENTJ',
                'enfp': 'ENFP',
                'enfj': 'ENFJ',
                'estp': 'ESTP',
                'estj': 'ESTJ',
                'esfp': 'ESFP',
                'esfj': 'ESFJ'
            }
            print(f'Hasil MBTI kamu adalah {mbti_types.get(mbti, "tipe tidak dikenal")}')
        else:
            print('Input tidak valid, coba lagi.')
        
        # Tanyakan apakah ingin mengulang
        repeat = input('Apakah anda ingin melakukan test lagi? (ya/tidak): ').strip().lower()
        if repeat != 'ya':
            print('Terima kasih, sampai jumpa!')
            break
            
    elif enter == 'tidak':
        print('Bye, sampai jumpa!')
        break
    
    else:
        print('Input tidak valid, coba lagi.')

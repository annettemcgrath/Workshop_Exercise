def quality_scaling(filename, N_removal, encoding):
    Sangardic={}	
    Solexadic={}
    Illumina18dic={}
    quality_scale_dict={}
    quality_char_dict={}
    read_sequence_dict={}
    read_name=[]

    chars = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHI'
    n = 0					
    for char in chars:
        Sangardic[char] = n
        n += 1

    chars = ';<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefgh'
    n = -5					
    for char in chars:
        Solexadic[char] = n
        n += 1

    chars = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJ'
    n = 0					
    for char in chars:
        Illumina18[char] = n
        n += 1


    fh = open(filename, 'r')
    readnameline = fh.readline()
    read_number = 0
    while readnameline != '':
        read_name[read_nember]=readnameline
        read_sequence=fh.readline()
        read_sequence_dict[read_name[read_number]]=read-sequence
        if N_removal==False: 
            secondheader=fh.readline()
            read_qual_char=fh.readline()
            quality_char_dict[read_name[read_number]]=read-qual_char
            read_qual_scale=[] 
            for i in len(read_qual_char):
                if encoding=='Sangar':
                    read_qual_scale.append(Sangardic[read_qual_char[i]])
                elif encoding=="Solexa":
                    read_qual_scale.append(Solexadic[read_qual_char[i]])		
                elif encoding=="Illumina 1.3":
                    read_qual_scale.append(Solexadic[read_qual_char[i]])
                elif encoding=="Illumina 1.5":
                    read_qual_scale.append(Solexadic[read_qual_char[i]])
                elif encoding=="Illumina 1.8":
                    read_qual_scale.append(Illumina8dic[read_qual_char[i]])
             quality_scale_dict[read_name[read_number]]=read-qual_scale

        else:
            if 'N' not in read_sequence:
                secondheader=fh.readline()
                read_qual_char=fh.readline()
                read_qual_scale=[] 
                for i in len(read_qual_char):
                    if encoding=='Sangar':
                        read_qual_scale.append(Sangardic[read_qual_char[i]])
                    elif encoding=="Solexa":
                        read_qual_scale.append(Solexadic[read_qual_char[i]])		
                    elif encoding=="Illumina 1.3":
                        read_qual_scale.append(Solexadic[read_qual_char[i]])
                    elif encoding=="Illumina 1.5":
                        read_qual_scale.append(Solexadic[read_qual_char[i]])
                    elif encoding=="Illumina 1.8":
                        read_qual_scale.append(Illumina8dic[read_qual_char[i]])
                quality_scale_dict[read_name[read_number]]=read-qual_scale

            else:
                secondheader=fh.readline()
                read_qual_char=fh.readline()             
                quality_scale_dict[read_name[read_number]]=[]
        readnameline = fh.readline()
        read_number += 1
     
    return  read_name,read_sequence_dict,quality_char_dict, quality_scale_dict,numberofreads=read_number 	


	


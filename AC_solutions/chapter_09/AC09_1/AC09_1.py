def create_output_file(name_ouput, sound, byte_array, _help):
    length_bytes = len(byte_array) // 2
    length_in_bytes = length_bytes.to_bytes(4, byteorder='little')
    length_in_bytes_with_header = (length_bytes + 36) \
        .to_bytes(4, byteorder='little')

    with open(name_ouput, 'wb') as split_file:
        split_file.write(_help[0:4])
        split_file.write(length_in_bytes_with_header)
        split_file.write(_help[8:40])
        split_file.write(length_in_bytes)

        for i in range(len(byte_array) // 2):
            byte_audio = byte_array[
                2 * i + int(sound)].to_bytes(1, byteorder='little')
            split_file.write(byte_audio)


with open('music.wav', 'rb') as weird_audio:
    file_header = bytearray(weird_audio.read(44))
    content_bytes = bytearray(weird_audio.read())

create_output_file('song1.wav', True, content_bytes, file_header)
create_output_file('song2.wav', False, content_bytes, file_header)

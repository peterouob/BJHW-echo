# Create echo server 

1. TCP 
2. UDP 
3. ICMP
 
## Experience   
- use icmp server need sudo Permissions
- when the packet have data only one byte for one format
    - struct.pack("bbHHhsssss", packet_type, code, checksum, packet_id, sequence, b"h", b"e", b"l", b"l", b"o")
- checksum is the most difficult
  1. `checksum = 0` 初始化校驗和為零
  2. `count_to = (len(data) // 2) * 2` 計算偶數部分
  3. `for count in range(0, count_to, 2)` 使用for迴圈去跑且一次走兩步
  4. `this_val = data[count + 1] * 256 + data[count]` 將相鄰的包計算為val(因此才一次走兩步)
  5. `checksum += this_val` 計算for range總和
  6. `checksum &= 0xffffffff` 確保效驗不超過32位元，避免計算溢出
  7. `if count_to < len(data)` 如果data為奇數再為他重新計算
  8. `checksum = (checksum >> 16) + (checksum & 0xffff)` 進行一個特殊的位運算，將校驗和的高 16 位和低 16 位相加。目的是確保進位結果在16位內且處理進位問題
  9. `checksum += (checksum >> 16)` 如果上一步操作導致進位，將進位部分再次加到校驗和中。
  10. `checksum = ~checksum & 0xffff` 這個步驟確保最終的校驗和是一個 16 位的值，並且是將校驗和的按位反轉。接收方可以使用相同的算法重新計算校驗和，並檢測數據是否在傳輸過程中被更改或損壞。
    - `~checksum` 將校驗和的所有位元進行按位取反。
    - `& 0xffff` 將結果與 16 位的全 1 數字進行按位與操作，這樣做的效果是將高於 16 位的部分清零。
  

inf = 99999999999

infs = [inf, inf, inf, inf]

way = [0, 1, 2, 3]

router_distance = {
    0: [
        [0, 1, 3, 7],
        infs.copy(),
        infs.copy(),
        infs.copy()
    ],
    1: [
        infs.copy(),
        [1, 0, 1, inf],
        infs.copy(),
        infs.copy()
    ],
    2: [
        infs.copy(),
        infs.copy(),
        [3, 1, 0, 2],
        infs.copy()
    ],
    3: [
        infs.copy(),
        infs.copy(),
        infs.copy(),
        [7, inf, 2, 0]
    ]}

neigbours = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}

router_distance

queues = {0: [], 1: [], 2: [], 3: []}

ways = [way.copy(), way.copy(), way.copy(), way.copy()]

N = 4

def recalc_distance(id, send=False):
    is_need_recalc = send
    for i, dists in queues[id]:
        for j in range(N):
            # print(id, i, j, queues[id], router_distance[id])
            if dists[j] < router_distance[id][i][j]:
                # print(i, j)
                router_distance[id][i][j] = dists[j]
                # ways[id][j] = i
                is_need_recalc = True
            
            if dists[j] < router_distance[id][j][i]:
                # print(i, j)
                router_distance[id][j][i] = dists[j]
                # ways[id][j] = i
                is_need_recalc = True
            
    queues[id] = []

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if router_distance[id][i][k] > router_distance[id][i][j] + router_distance[id][j][k]:
                    router_distance[id][i][k] = router_distance[id][i][j] + router_distance[id][j][k]

    if is_need_recalc:
        for id2 in neigbours[id]:
            queues[id2].append((id, router_distance[id][id]))

    
for id in range(N):
    recalc_distance(id, True)

    # print(router_distance)

def launch():
    while 1:
        is_ended = True
        for id in range(N):
            if len(queues[id]) > 0:
                is_ended = False
                recalc_distance(id)

        if is_ended:
            break

launch()

def show(arr):
    print('\n'.join([' '.join([str(i) for i in r]) for r in arr]))


# print('ways: ')

# show(ways)

print('router_distance: ')

show(router_distance[0])

router_distance[0][0][3] = 1
    
recalc_distance(0, True)

launch()

print('new_distance: ')

show(router_distance[0])








































# import socket

# import struct

# hostAddress   = "5.189.198.226"
# bufferSize    = 1024

# timeout= 5.0

# # Create a UDP socket at client side
# ICMPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_ICMP)

# # Send to server using created UDP socket

# # ICMPClientSocket.sendto(serverAddressPort)

# print(socket.getprotobyname("icmp"))

# class ICMPMessage():
#     def __init__(self, type=8, code=0, checksum=0, identifier=0, sequence_number=0, payload=b''):
#         self.type = type
#         self.code = code
#         self.checksum = checksum
#         self.identifier = identifier
#         self.sequence_number = sequence_number
#         self.payload = payload

#     def calculated_checksum(self):
#         data = struct.pack('>BBHHH', self.type, self.code, 0, self.identifier, self.sequence_number) + self.payload
#         if len(data) & 0x1:
#             data += b'\0'
#         checksum = 0
#         for pos in range(0, len(data), 2):
#             b1 = data[pos]
#             b2 = data[pos + 1]
#             checksum += (b1 << 8) + b2
#         while checksum >= 0x10000:
#             checksum = (checksum & 0xffff) + (checksum >> 16)
#         checksum = ~checksum & 0xffff
#         return checksum

#      def valid_checksum(self):
#         return self.checksum == self.calculated_checksum

#     def to_bytes(self):
#         return struct.pack('>BBHHH', self.type, self.code, self.checksum, self.identifier, self.sequence_number) + self.payload

#     def from_bytes(data):
#         if len(data) < 8:
#             raise ValueError('ICMP Echo packet must be at least 8 bytes')
#         ret = IcmpEcho()
#         ret.payload = data[8:]
#         header = struct.unpack('>BBHHH', data[0:8])
#         ret.type = header[0]
#         if ret.type not in (0, 8):
#             raise ValueError('Not a ICMP Echo message (type={type})'.format(type=ret.type))
#         ret.code = header[1]
#         ret.checksum = header[2]
#         ret.identifier = header[3]
#         ret.sequence_number = header[4]
#         return ret
 
# for iteration in range(1, 64):

#     irequest = IcmpEcho(payload=os.urandom(32))
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_ICMP) as s:
#         s.connect(hostAddress)
#         s.settimeout(timeout)

#         start = time.clock_gettime(time.CLOCK_MONOTONIC)
#         s.send(request.to_bytes())
#         response = s.recv(65536)
#         end = time.clock_gettime(time.CLOCK_MONOTONIC)

#     response = IcmpEcho.from_bytes(response)
#     rtt_ms = (end - start) * 1000
#     print('Got response in {delay:.3f} ms'.format(delay=rtt_ms))


#     command = input()
#     bytesToSend = str.encode(command)

#     ICMPClientSocket.sendall(bytesToSend)

#     msgFromServer = ICMPClientSocket.recv(bufferSize)
#     msg = msgFromServer.decode("utf-8") 

#     print(msg)
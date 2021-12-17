with open('Day16/test_input.txt') as f:
    data = f.readlines()[0].rstrip()


class Packet():
    def __init__(self, version, type_id, number, parent=None):
        self.version = version
        self.id = type_id
        self.parent = parent
        self.number = number

    def __repr__(self):
        return f"|Version: {self.version}, Type ID: {self.id}, Number: {self.number}|"


class PacketReader:
    def __init__(self, hexa_input):
        self.input = bin(int(hexa_input, 16))[2:]
        if len(self.input) % 4:
            self.input = self.input.zfill(
                len(self.input) + (4-len(self.input) % 4))
        self.pointer = 0
        self.types = {4: self.literal}
        self.packets = []

    def get_int(self, length):
        self.pointer += length
        return int(self.input[self.pointer-length:self.pointer], 2)

    def get_bits(self, length):
        self.pointer += length
        return self.input[self.pointer-length:self.pointer]

    def literal(self):
        last_digit = False
        bits = ''
        while not last_digit:
            if self.input[self.pointer] == '0':
                last_digit = True
            self.pointer += 1
            bits = bits + self.get_bits(4)

        return int(bits, 2)

    def operator(self):
        if self.input[self.pointer] == '0':
            self.pointer += 1
            total_sub_packet_length = self.get_int(15)
            limit = self.pointer + total_sub_packet_length
            while self.pointer < limit:
                self.read()
        elif self.input[self.pointer] == '1':
            self.pointer += 1
            num_sub_packets = self.get_int(11)
            for _ in range(num_sub_packets):
                self.read()

    def read(self):
        version = self.get_int(3)
        type_id = self.get_int(3)
        number = self.types.get(type_id, self.operator)()

        packet = Packet(version, type_id, number)
        self.packets.append(packet)

        return packet


reader = PacketReader(data)
reader.read()

print(sum([packet.version for packet in reader.packets]))

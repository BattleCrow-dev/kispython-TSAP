from pprint import pprint
import struct

# Интересное, но не принимаемое за отличное от первого
class DataParser:
    SIGNATURE = b"\x57\x47\x51\x55\x88"

    def __init__(self, binary_data):
        self.binary_data = binary_data
        self.offset = 5

    def parse(self):
        if self.binary_data[:5] != self.SIGNATURE:
            return None

        A1, A2, A3_size, A3_addr, A4_addr, A5_size, A5_addr, A6, A7, A8 = (
            struct.unpack_from(
                "<qBHIIHHhhh", self.binary_data, self.offset))

        B1, B2 = struct.unpack_from("<HH", self.binary_data, A4_addr)

        C_data = self._parse_C_data(A5_size, A5_addr)

        result = {
            'A1': A1,
            'A2': A2,
            'A3': self.binary_data[A3_addr:A3_addr + A3_size].decode("utf-8"),
            'A4': {'B1': B1, 'B2': B2},
            'A5': C_data,
            'A6': A6,
            'A7': A7,
            'A8': A8
        }

        return result

    def _parse_C_data(self, A5_size, A5_addr):
        C_data = []
        for i in range(A5_size):
            temp_addr = struct.unpack_from(
                "H", self.binary_data, A5_addr + i * 2)
            temp = struct.unpack_from(
                "<bI", self.binary_data, temp_addr[0])

            D1_0, D1_1, D1_2, D2_size, D2_addr = struct.unpack_from(
                "<HHHHI", self.binary_data, temp[1])

            c_instance = {
                "C1": temp[0],
                "C2": {
                    "D1": [D1_0, D1_1, D1_2],
                    "D2": list(struct.unpack(
                        f"<{D2_size}Q",
                        self.binary_data[D2_addr:D2_addr + D2_size * 8]))
                }
            }
            C_data.append(c_instance)

        return C_data


# 1-ое по популярности
def main(binary_data):
    signature = b"\x57\x47\x51\x55\x88"

    if binary_data[:5] != signature:
        return None

    offset = 5
    (
        A1,
        A2,
        A3_size,
        A3_addr,
        A4_addr,
        A5_size,
        A5_addr,
        A6,
        A7,
        A8
    ) = struct.unpack_from("<qBHIIHHhhh", binary_data, offset)

    (
        B1,
        B2
    ) = struct.unpack_from("<HH", binary_data, A4_addr)

    C_data = []
    for i in range(0, A5_size):
        temp_addr = struct.unpack_from(
            "H", binary_data, A5_addr + i * 2)
        temp = struct.unpack_from("<bI", binary_data, temp_addr[0])

        (
            D1_0,
            D1_1,
            D1_2,
            D2_size,
            D2_addr
        ) = struct.unpack_from("<HHHHI", binary_data, temp[1])

        c_instance = {
            "C1": temp[0],
            "C2": {
                "D1": [D1_0, D1_1, D1_2],
                "D2": list(struct.unpack(
                    f"<{D2_size}Q",
                    binary_data[D2_addr:D2_addr + D2_size * 8]))
            }
        }
        C_data.append(c_instance)

    result = {
        'A1': A1,
        'A2': A2,
        'A3': binary_data[A3_addr:A3_addr + A3_size].decode("utf-8"),
        'A4':
            {
                'B1': B1,
                'B2': B2
            },
        'A5': C_data,
        'A6': A6,
        'A7': A7,
        'A8': A8
    }

    return result


def test():
    pprint(DataParser(b'WGQU\x88\x03\xa8Q+\x9b\xe8\t\xd5\xbf\x02\x00"\x00\x00\x00$\x00\x00\x00\x02\x00j\x00\xdeH~1\xdc\xf5vcR\x07`\xe9XT\xad\x92\xdd\x13\xa9l\xb3\xab\x88*\xd8t\x89\xe7\xdc{R\xe6[\xef\x02\x00(\x00\x00\x00\xf88\x00\x00\x00\xcbBu\xdd\xf7/$7}\xf9\xe6\xe6oOZ\xb5\xcb\xb2\xf8\x0fDg\x02\x00I\x00\x00\x00jY\x00\x00\x00D\x00e\x00').parse())
    print("---OwO---")
    pprint(main(b'WGQU\x88\x03\xa8Q+\x9b\xe8\t\xd5\xbf\x02\x00"\x00\x00\x00$\x00\x00\x00\x02\x00j\x00\xdeH~1\xdc\xf5vcR\x07`\xe9XT\xad\x92\xdd\x13\xa9l\xb3\xab\x88*\xd8t\x89\xe7\xdc{R\xe6[\xef\x02\x00(\x00\x00\x00\xf88\x00\x00\x00\xcbBu\xdd\xf7/$7}\xf9\xe6\xe6oOZ\xb5\xcb\xb2\xf8\x0fDg\x02\x00I\x00\x00\x00jY\x00\x00\x00D\x00e\x00'))
    print("---OwO---")
    pprint(DataParser(b'WGQU\x88\xd9\x8d\xe9~\x8d.2|\xc5\x02\x00"\x00\x00\x00$\x00\x00\x00\x02\x00j\x00\xc9\xa5\xd4\x0bg\xa1do\xec\x00\xc0\xc8\xa6\x1d\xe3\xf17\x07G\x16m\x0c-\xdaiT\xf6G\xd3\xc7\x9e.N\x1b\x02\x00(\x00\x00\x00`8\x00\x00\x00&,\xf1\xc86&\xf7Q\xe1K6\x0e\x01\x96\x04@\x1c\xa6\x0eS\xd6\x95\x02\x00I\x00\x00\x00\x82Y\x00\x00\x00D\x00e\x00').parse())
    print("---OwO---")
    pprint(main(b'WGQU\x88\xd9\x8d\xe9~\x8d.2|\xc5\x02\x00"\x00\x00\x00$\x00\x00\x00\x02\x00j\x00\xc9\xa5\xd4\x0bg\xa1do\xec\x00\xc0\xc8\xa6\x1d\xe3\xf17\x07G\x16m\x0c-\xdaiT\xf6G\xd3\xc7\x9e.N\x1b\x02\x00(\x00\x00\x00`8\x00\x00\x00&,\xf1\xc86&\xf7Q\xe1K6\x0e\x01\x96\x04@\x1c\xa6\x0eS\xd6\x95\x02\x00I\x00\x00\x00\x82Y\x00\x00\x00D\x00e\x00'))


test()
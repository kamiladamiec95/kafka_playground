from confluent_kafka.serialization import StringSerializer


serializer_default = StringSerializer()
serializer_utf8 = StringSerializer("utf-8")
serializer_utf16 = StringSerializer("utf-16")
serializer_utf32 = StringSerializer("utf-32")
direct_utf8 = "hello world".encode("utf-8")
direct_utf16 = "hello world".encode("utf-16")

serialized_default = serializer_default("hello world")
serialized_utf8 = serializer_utf8("hello world", None)
serialized_utf16 = serializer_utf16("hello world", None)
serialized_utf32 = serializer_utf32("hello world", None)

#print(direct)
print(serialized_default)
print(serialized_utf8)
print(serialized_utf16)
print(serialized_utf32)

print(direct_utf8 == serialized_utf8 == serialized_default)
print(direct_utf16 == serialized_utf16)
import re


class PublicIdentifier:

    # Legacy only needed till we update Core.BE Custodian's configuration (team/project IDs) Pivotal #163298101
    LEGACY_ID_PATTERN = re.compile('[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
    GENERIC_ID_PATTERN = re.compile('entity_[a-fA-F0-9]{16}')
    LEGACY_CARDHOLDER_ID_PATTERN = re.compile('crdhldr_[a-fA-F0-9]{16}')
    CARDHOLDER_ID_PATTERN = re.compile('crdhldr_[a-fA-F0-9]{20}')
    GENERIC_ID_HEADER = 'entity_'

    @classmethod
    def _create_fixed_hash(cls, value):

        # Produce an integer hash of a 64-bit integer, returning a transformed 64-bit
        # integer
        value = (0x3B79DB6A ^ value) * 0x72F8B3AF
        return value >> (value & 0xF) & 0xFFFFFFFF

    @classmethod
    def _transcode(cls, value):

        # Reversibly _transcode a 128-bit integer to a scrambled form, returning a
        # new 128-bit integer
        right = value & 0xFFFFFFFF
        left = (value >> 32 & 0xFFFFFFFF)
        left_masked = left ^ cls._create_fixed_hash(value=right)
        right_masked = right ^ cls._create_fixed_hash(value=left_masked)
        return (right_masked << 32) + left_masked

    @classmethod
    def _decode_legacy_public_id(cls, public_id):

        # Delete the '-' which simulates UUID format, and decode
        public_id_plain_format = public_id.replace('-', '')
        return LegacyIdTranscoder.transcode(value=int(public_id_plain_format, 16))

    @classmethod
    def _decode_generic_public_id(cls, public_id):

        # Remove class header and decode
        split_public_id = public_id.split(cls.GENERIC_ID_HEADER)
        return cls._transcode(value=int(split_public_id[1], 16))

    @classmethod
    def _decode_cardholder_public_id(cls, public_id, context):

        # User public ID is random, match is in data base (pl_directory)
        return context.decode_public_user_id(public_id=public_id)

    @classmethod
    def encode(cls, db_id, context=None):

        # Method to create the public identifier from the
        # data base identifier. The relation will be one-to-one:
        # one db-id will produce always the same public-id

        # If not defined, maintain it as not defined
        if db_id is None:
            return None

        # Transcode the DB identifier and return it as an 16-character hex string
        # adding the appropriate header
        return cls.GENERIC_ID_HEADER + '%016x' % cls._transcode(value=db_id)

    @classmethod
    def decode(cls, public_id, context=None):

        # Method to obtain the data base identifier from its public
        # identifier. The relation will be one-to-one: one public-id
        # will produce always the same db-id

        # If not defined, maintain it as not defined
        if public_id is None:
            return None

        # Legacy UUID format (necessary backward compatibility for the
        # team-id / project-id currently set as Custodian config in the
        # Core.BE
        if cls.LEGACY_ID_PATTERN.match(public_id) is not None:
            return cls._decode_legacy_public_id(public_id=public_id)

        elif cls.GENERIC_ID_PATTERN.match(public_id) is not None:
            return cls._decode_generic_public_id(public_id=public_id)

        elif cls.CARDHOLDER_ID_PATTERN.match(public_id) is not None:
            return cls._decode_cardholder_public_id(public_id=public_id,
                                                    context=context)

        elif cls.LEGACY_CARDHOLDER_ID_PATTERN.match(public_id) is not None:
            return cls._decode_cardholder_public_id(public_id=public_id,
                                                    context=context)

        return None


# this class keeps all functionality, but changes in this subclass just only some class variables
class PublicCorporationIdentifier(PublicIdentifier):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        
    GENERIC_ID_PATTERN = re.compile('corporation_[a-fA-F0-9]{16}')
    GENERIC_ID_HEADER = 'corporation_'


# Legacy only needed till we update Core.BE Custodian's configuration (team/project IDs) Pivotal #163298101
class LegacyIdTranscoder:

    @classmethod
    def _create_fixed_hash(cls, value):
        value = (0x3B79DB6A2CE58A24 ^ value) * 0x72F8B3AF923C9E96
        return value >> (value & 0xF) & 0xFFFFFFFFFFFFFFFF

    @classmethod
    def transcode(cls, value):
        right = value & 0xFFFFFFFFFFFFFFFF
        left = value >> 64 & 0xFFFFFFFFFFFFFFFF ^ cls._create_fixed_hash(value=right)
        return ((right ^ cls._create_fixed_hash(value=left)) << 64) + left


public_identifier_1 = PublicIdentifier.encode(23)
public_identifier_2 = PublicCorporationIdentifier.encode(23)

print(PublicCorporationIdentifier.decode(public_identifier_1))

print('public identifier:             {0}'.format(public_identifier_1))
print('public corporation identifier: {0}'.format(public_identifier_2))

public_identifier_3 = PublicIdentifier.decode(public_identifier_1)
public_identifier_4 = PublicCorporationIdentifier.decode(public_identifier_2)

print('identifier:             {0}'.format(public_identifier_3))
print('corporation identifier: {0}'.format(public_identifier_4))
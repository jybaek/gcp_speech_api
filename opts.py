def add_basic_args(parser):
    parser.add_argument('--audio-path', default='test.raw', help='Audio file to convert to text.')
    parser.add_argument('--language-code', default='ko-KR', help='Language code. ( ko-KR, en-US, etc.. )')
    return parser

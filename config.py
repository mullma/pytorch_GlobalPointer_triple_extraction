import argparse


class Args:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser()
        return parser

    @staticmethod
    def initialize(parser):
        # args for path
        parser.add_argument('--output_dir', default='./checkpoints/',
                            help='the output dir for model checkpoints')

        parser.add_argument('--bert_dir', default='./model_hub/albert-base-chinese/',
                            help='bert dir for uer')
        parser.add_argument('--data_dir', default='./data/cner/',
                            help='data dir for uer')
        parser.add_argument('--log_dir', default='./logs/',
                            help='log dir for uer')

        # other args
        parser.add_argument('--num_tags', default=49, type=int,
                            help='number of tags')
        parser.add_argument('--seed', type=int, default=123, help='random seed')

        parser.add_argument('--gpu_ids', type=str, default='-1',
                            help='gpu ids to use, -1 for cpu, "0,1" for multi gpu')

        parser.add_argument('--max_seq_len', default=256, type=int)

        parser.add_argument('--eval_batch_size', default=12, type=int)


        # train args
        parser.add_argument('--train_epochs', default=15, type=int,
                            help='Max training epoch')

        parser.add_argument('--dropout_prob', default=0.1, type=float,
                            help='drop out probability')

        # 2e-5
        parser.add_argument('--lr', default=1e-5, type=float,
                            help='bert学习率')
        # 2e-3
        parser.add_argument('--other_lr', default=3e-4, type=float,
                            help='bilstm和多层感知机学习率')
        # 0.5
        parser.add_argument('--max_grad_norm', default=1, type=float,
                            help='max grad clip')
        parser.add_argument('--use_tensorboard', default="True",
                            help='max grad clip')

        parser.add_argument('--warmup_proportion', default=0.1, type=float)

        parser.add_argument('--weight_decay', default=0.01, type=float)

        parser.add_argument('--adam_epsilon', default=1e-8, type=float)

        parser.add_argument('--train_batch_size', default=32, type=int)
        parser.add_argument('--use_dev_num', default=32, type=int, help="用于验证和测试的数量")
        parser.add_argument('--eval_steps', default=32, type=int, help="多少步进行验证")



        return parser

    def get_parser(self):
        parser = self.parse()
        parser = self.initialize(parser)
        return parser.parse_args()
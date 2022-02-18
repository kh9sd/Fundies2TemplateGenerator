import logging.config
from abstract_syntax_tree.ast_processor import AstProcessor
from abstract_syntax_tree.basic_info_listener import BasicInfoListener


if __name__ == '__main__':
    # logging_setting_path = "C:\\Users\\kevin\\Desktop\\Fundies2TemplateGenerator\\log.log"
    # logging.config.fileConfig(logging_setting_path)
    logger = logging.getLogger(__file__)

    target_file_path = "C:\\Users\\kevin\\Desktop\\Fundies2TemplateGenerator\\TourInfoServiceImpl.java"

    #★ Point 1
    ast_info = AstProcessor(logging, BasicInfoListener()).execute(target_file_path)

    print(ast_info)

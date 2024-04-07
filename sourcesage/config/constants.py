import os

class Constants:
    def __init__(self, output_dir, owner, repository):
        self.OWNER = owner
        self.REPOSITORY = repository
        self.ISSUES_FILE_NAME = "open_issues_filtered.json"

        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.REPO_PATH = self.BASE_DIR
        self.CONFIG_DIR = os.path.join(self.BASE_DIR, 'config')
        self.DOCS_DIR = os.path.join(self.BASE_DIR, "config")

        self.LANGUAGE_MAP_FILE = os.path.join(self.CONFIG_DIR, 'language_map.json')
        self.IGNORE_FILE = os.path.join(self.CONFIG_DIR, '.SourceSageignore')

        self.SOURCE_SAGE_MD = "DocuMind.md"
        self.CHANGELOG_DIR = "Changelog"
        self.STAGED_DIFF_MD = "STAGED_DIFF.md"

        self.set_output_dir(output_dir)

    def set_output_dir(self, output_dir):
        self.SOURCE_SAGE_ASSETS_DIR = os.path.join(output_dir, "SourceSageAssets")
        self.ISSUE_LOG_DIR = os.path.join(self.SOURCE_SAGE_ASSETS_DIR, "ISSUE_LOG")
        self.ISSUES_RESOLVE_DIR = os.path.join(self.SOURCE_SAGE_ASSETS_DIR, "ISSUE_WISE/ISSUES_RESOLVE")
        self.STAGE_INFO_DIR = os.path.join(self.SOURCE_SAGE_ASSETS_DIR, "COMMIT_CRAFT/STAGE_INFO")

        self.TEMPLATE_ISSUES_RESOLVE_DIR = os.path.join(self.DOCS_DIR, "ISSUES_RESOLVE")
        self.ISSUES_RESOLVE_TEMPLATE_MD = "ISSUES_RESOLVE_TEMPLATE.md"

        self.TEMPLATE_STAGE_INFO_DIR = os.path.join(self.DOCS_DIR, "STAGE_INFO")
        self.STAGE_INFO_OUTPUT_MD = "STAGE_INFO_AND_ISSUES_AND_PROMT.md"
        self.STAGE_INFO_TEMPLATE_MD = "STAGE_INFO_AND_ISSUES_TEMPLATE.md"

        self.STAGE_INFO_SIMPLE_OUTPUT_MD = "STAGE_INFO_AND_PROMT.md"
        self.STAGE_INFO_SIMPLE_TEMPLATE_MD = "STAGE_INFO_TEMPLATE.md"
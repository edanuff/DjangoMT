
from django.db import models

class Author(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'author_id')
    api_password = models.CharField(max_length = 180, blank = True, db_column = 'author_api_password')
    auth_type = models.CharField(max_length = 150, blank = True, db_column = 'author_auth_type')
    basename = models.CharField(max_length = 765, blank = True, db_column = 'author_basename')
    can_create_blog = models.IntegerField(null = True, blank = True, db_column = 'author_can_create_blog')
    can_view_log = models.IntegerField(null = True, blank = True, db_column = 'author_can_view_log')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'author_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'author_created_on')
    email = models.CharField(max_length = 225, blank = True, db_column = 'author_email')
    entry_prefs = models.CharField(max_length = 765, blank = True, db_column = 'author_entry_prefs')
    external_id = models.CharField(max_length = 765, blank = True, db_column = 'author_external_id')
    hint = models.CharField(max_length = 225, blank = True, db_column = 'author_hint')
    is_superuser = models.IntegerField(null = True, blank = True, db_column = 'author_is_superuser')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'author_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'author_modified_on')
    name = models.CharField(max_length = 765, db_column = 'author_name')
    nickname = models.CharField(max_length = 765, blank = True, db_column = 'author_nickname')
    password = models.CharField(max_length = 180, db_column = 'author_password')
    preferred_language = models.CharField(max_length = 150, blank = True, db_column = 'author_preferred_language')
    public_key = models.TextField(blank = True, db_column = 'author_public_key')
    remote_auth_token = models.CharField(max_length = 150, blank = True, db_column = 'author_remote_auth_token')
    remote_auth_username = models.CharField(max_length = 150, blank = True, db_column = 'author_remote_auth_username')
    status = models.IntegerField(null = True, blank = True, db_column = 'author_status')
    text_format = models.CharField(max_length = 90, blank = True, db_column = 'author_text_format')
    type_field = models.IntegerField(db_column = 'author_type')
    url = models.CharField(max_length = 765, blank = True, db_column = 'author_url')
    userpic_asset_id = models.IntegerField(null = True, blank = True, db_column = 'author_userpic_asset_id')
    class Meta:
        db_table = u'mt_author'

class AuthorMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'author_meta_author_id')
    type_field = models.CharField(max_length = 225, db_column = 'author_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'author_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'author_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'author_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'author_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'author_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'author_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'author_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'author_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'author_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'author_meta_vclob')
    class Meta:
        db_table = u'mt_author_meta'

class Blog(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'blog_id')
    allow_anon_comments = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_anon_comments')
    allow_comment_html = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_comment_html')
    allow_commenter_regist = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_commenter_regist')
    allow_comments_default = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_comments_default')
    allow_pings = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_pings')
    allow_pings_default = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_pings_default')
    allow_reg_comments = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_reg_comments')
    allow_unreg_comments = models.IntegerField(null = True, blank = True, db_column = 'blog_allow_unreg_comments')
    archive_path = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_path')
    archive_tmpl_category = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_tmpl_category')
    archive_tmpl_daily = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_tmpl_daily')
    archive_tmpl_individual = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_tmpl_individual')
    archive_tmpl_monthly = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_tmpl_monthly')
    archive_tmpl_weekly = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_tmpl_weekly')
    archive_type = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_type')
    archive_type_preferred = models.CharField(max_length = 75, blank = True, db_column = 'blog_archive_type_preferred')
    archive_url = models.CharField(max_length = 765, blank = True, db_column = 'blog_archive_url')
    autodiscover_links = models.IntegerField(null = True, blank = True, db_column = 'blog_autodiscover_links')
    autolink_urls = models.IntegerField(null = True, blank = True, db_column = 'blog_autolink_urls')
    basename_limit = models.IntegerField(null = True, blank = True, db_column = 'blog_basename_limit')
    cc_license = models.CharField(max_length = 765, blank = True, db_column = 'blog_cc_license')
    children_modified_on = models.DateTimeField(null = True, blank = True, db_column = 'blog_children_modified_on')
    convert_paras = models.CharField(max_length = 90, blank = True, db_column = 'blog_convert_paras')
    convert_paras_comments = models.CharField(max_length = 90, blank = True, db_column = 'blog_convert_paras_comments')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'blog_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'blog_created_on')
    custom_dynamic_templates = models.CharField(max_length = 75, blank = True, db_column = 'blog_custom_dynamic_templates')
    days_on_index = models.IntegerField(null = True, blank = True, db_column = 'blog_days_on_index')
    description = models.TextField(blank = True, db_column = 'blog_description')
    email_new_comments = models.IntegerField(null = True, blank = True, db_column = 'blog_email_new_comments')
    email_new_pings = models.IntegerField(null = True, blank = True, db_column = 'blog_email_new_pings')
    entries_on_index = models.IntegerField(null = True, blank = True, db_column = 'blog_entries_on_index')
    file_extension = models.CharField(max_length = 30, blank = True, db_column = 'blog_file_extension')
    google_api_key = models.CharField(max_length = 96, blank = True, db_column = 'blog_google_api_key')
    internal_autodiscovery = models.IntegerField(null = True, blank = True, db_column = 'blog_internal_autodiscovery')
    is_dynamic = models.IntegerField(null = True, blank = True, db_column = 'blog_is_dynamic')
    junk_folder_expiry = models.IntegerField(null = True, blank = True, db_column = 'blog_junk_folder_expiry')
    junk_score_threshold = models.FloatField(null = True, blank = True, db_column = 'blog_junk_score_threshold')
    language = models.CharField(max_length = 15, blank = True, db_column = 'blog_language')
    manual_approve_commenters = models.IntegerField(null = True, blank = True, db_column = 'blog_manual_approve_commenters')
    moderate_pings = models.IntegerField(null = True, blank = True, db_column = 'blog_moderate_pings')
    moderate_unreg_comments = models.IntegerField(null = True, blank = True, db_column = 'blog_moderate_unreg_comments')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'blog_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'blog_modified_on')
    mt_update_key = models.CharField(max_length = 90, blank = True, db_column = 'blog_mt_update_key')
    name = models.CharField(max_length = 765, db_column = 'blog_name')
    old_style_archive_links = models.IntegerField(null = True, blank = True, db_column = 'blog_old_style_archive_links')
    ping_blogs = models.IntegerField(null = True, blank = True, db_column = 'blog_ping_blogs')
    ping_google = models.IntegerField(null = True, blank = True, db_column = 'blog_ping_google')
    ping_others = models.TextField(blank = True, db_column = 'blog_ping_others')
    ping_technorati = models.IntegerField(null = True, blank = True, db_column = 'blog_ping_technorati')
    ping_weblogs = models.IntegerField(null = True, blank = True, db_column = 'blog_ping_weblogs')
    remote_auth_token = models.CharField(max_length = 150, blank = True, db_column = 'blog_remote_auth_token')
    require_comment_emails = models.IntegerField(null = True, blank = True, db_column = 'blog_require_comment_emails')
    sanitize_spec = models.CharField(max_length = 765, blank = True, db_column = 'blog_sanitize_spec')
    server_offset = models.FloatField(null = True, blank = True, db_column = 'blog_server_offset')
    site_path = models.CharField(max_length = 765, blank = True, db_column = 'blog_site_path')
    site_url = models.CharField(max_length = 765, blank = True, db_column = 'blog_site_url')
    sort_order_comments = models.CharField(max_length = 24, blank = True, db_column = 'blog_sort_order_comments')
    sort_order_posts = models.CharField(max_length = 24, blank = True, db_column = 'blog_sort_order_posts')
    status_default = models.IntegerField(null = True, blank = True, db_column = 'blog_status_default')
    use_comment_confirmation = models.IntegerField(null = True, blank = True, db_column = 'blog_use_comment_confirmation')
    welcome_msg = models.TextField(blank = True, db_column = 'blog_welcome_msg')
    words_in_excerpt = models.IntegerField(null = True, blank = True, db_column = 'blog_words_in_excerpt')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'mt_blog'


class BlogMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'blog_meta_blog_id')
    type_field = models.CharField(max_length = 225, db_column = 'blog_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'blog_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'blog_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'blog_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'blog_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'blog_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'blog_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'blog_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'blog_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'blog_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'blog_meta_vclob')
    class Meta:
        db_table = u'mt_blog_meta'

class Role(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'role_id')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'role_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'role_created_on')
    description = models.TextField(blank = True, db_column = 'role_description')
    is_system = models.IntegerField(null = True, blank = True, db_column = 'role_is_system')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'role_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'role_modified_on')
    name = models.CharField(max_length = 765, db_column = 'role_name')
    permissions = models.TextField(blank = True, db_column = 'role_permissions')
    role_mask = models.IntegerField(null = True, blank = True, db_column = 'role_role_mask')
    role_mask2 = models.IntegerField(null = True, blank = True, db_column = 'role_role_mask2')
    role_mask3 = models.IntegerField(null = True, blank = True, db_column = 'role_role_mask3')
    role_mask4 = models.IntegerField(null = True, blank = True, db_column = 'role_role_mask4')
    class Meta:
        db_table = u'mt_role'

class Asset(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'asset_id')
    blog = models.ForeignKey(Blog, db_column = 'asset_blog_id', related_name='assets')
    class_field = models.CharField(max_length = 765, blank = True, db_column = 'asset_class')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'asset_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'asset_created_on')
    description = models.TextField(blank = True, db_column = 'asset_description')
    file_ext = models.CharField(max_length = 60, blank = True, db_column = 'asset_file_ext')
    file_name = models.CharField(max_length = 765, blank = True, db_column = 'asset_file_name')
    file_path = models.CharField(max_length = 765, blank = True, db_column = 'asset_file_path')
    label = models.CharField(max_length = 765, blank = True, db_column = 'asset_label')
    mime_type = models.CharField(max_length = 765, blank = True, db_column = 'asset_mime_type')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'asset_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'asset_modified_on')
    parent = models.ForeignKey('self', null = True, blank = True, db_column = 'asset_parent')
    url = models.CharField(max_length = 765, blank = True, db_column = 'asset_url')
    class Meta:
        db_table = u'mt_asset'

class AssetMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'asset_meta_asset_id')
    type_field = models.CharField(max_length = 225, db_column = 'asset_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'asset_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'asset_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'asset_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'asset_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'asset_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'asset_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'asset_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'asset_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'asset_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'asset_meta_vclob')
    class Meta:
        db_table = u'mt_asset_meta'

class Association(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'association_id')
    author = models.ForeignKey(Author, null = True, blank = True, db_column = 'association_author_id')
    blog = models.ForeignKey(Blog, null = True, blank = True, db_column = 'association_blog_id', related_name='associations')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'association_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'association_created_on')
    group_id = models.IntegerField(null = True, blank = True, db_column = 'association_group_id')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'association_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'association_modified_on')
    role = models.ForeignKey(Role, null = True, blank = True, db_column = 'association_role_id', related_name='associations')
    type_field = models.IntegerField(db_column = 'association_type')
    class Meta:
        db_table = u'mt_association'

class Category(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'category_id')
    allow_pings = models.IntegerField(null = True, blank = True, db_column = 'category_allow_pings')
    author = models.ForeignKey(Author, null = True, blank = True, db_column = 'category_author_id')
    basename = models.CharField(max_length = 765, blank = True, db_column = 'category_basename')
    blog = models.ForeignKey(Blog, db_column = 'category_blog_id', related_name='categories')
    class_field = models.CharField(max_length = 765, blank = True, db_column = 'category_class')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'category_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'category_created_on')
    description = models.TextField(blank = True, db_column = 'category_description')
    label = models.CharField(max_length = 300, db_column = 'category_label')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'category_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'category_modified_on')
    parent = models.ForeignKey('self', null = True, blank = True, db_column = 'category_parent', related_name='children')
    ping_urls = models.TextField(blank = True, db_column = 'category_ping_urls')
    def __unicode__(self):
        return self.label
    class Meta:
        db_table = u'mt_category'

class CategoryMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'category_meta_category_id')
    type_field = models.CharField(max_length = 225, db_column = 'category_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'category_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'category_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'category_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'category_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'category_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'category_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'category_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'category_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'category_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'category_meta_vclob')
    class Meta:
        db_table = u'mt_category_meta'

class Template(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'template_id')
    blog = models.ForeignKey(Blog, db_column = 'template_blog_id', related_name='templates')
    build_dynamic = models.IntegerField(null = True, blank = True, db_column = 'template_build_dynamic')
    build_interval = models.IntegerField(null = True, blank = True, db_column = 'template_build_interval')
    build_type = models.IntegerField(null = True, blank = True, db_column = 'template_build_type')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'template_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'template_created_on')
    identifier = models.CharField(max_length = 150, blank = True, db_column = 'template_identifier')
    linked_file = models.CharField(max_length = 765, blank = True, db_column = 'template_linked_file')
    linked_file_mtime = models.CharField(max_length = 30, blank = True, db_column = 'template_linked_file_mtime')
    linked_file_size = models.IntegerField(null = True, blank = True, db_column = 'template_linked_file_size')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'template_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'template_modified_on')
    name = models.CharField(max_length = 765, db_column = 'template_name')
    outfile = models.CharField(max_length = 765, blank = True, db_column = 'template_outfile')
    rebuild_me = models.IntegerField(null = True, blank = True, db_column = 'template_rebuild_me')
    text = models.TextField(blank = True, db_column = 'template_text')
    type_field = models.CharField(max_length = 75, db_column = 'template_type')
    class Meta:
        db_table = u'mt_template'

class TemplateMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'template_meta_template_id')
    type_field = models.CharField(max_length = 225, db_column = 'template_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'template_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'template_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'template_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'template_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'template_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'template_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'template_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'template_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'template_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'template_meta_vclob')
    class Meta:
        db_table = u'mt_template_meta'

class TemplateMap(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'templatemap_id')
    archive_type = models.CharField(max_length = 75, db_column = 'templatemap_archive_type')
    blog = models.ForeignKey(Blog, db_column = 'templatemap_blog_id')
    build_interval = models.IntegerField(null = True, blank = True, db_column = 'templatemap_build_interval')
    build_type = models.IntegerField(null = True, blank = True, db_column = 'templatemap_build_type')
    file_template = models.CharField(max_length = 765, blank = True, db_column = 'templatemap_file_template')
    is_preferred = models.IntegerField(null = True, blank = True, db_column = 'templatemap_is_preferred')
    template = models.ForeignKey(Template, db_column = 'templatemap_template_id')
    class Meta:
        db_table = u'mt_templatemap'

class Tag(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'tag_id')
    is_private = models.IntegerField(null = True, blank = True, db_column = 'tag_is_private')
    n8d_id = models.IntegerField(null = True, blank = True, db_column = 'tag_n8d_id')
    name = models.CharField(max_length = 765, db_column = 'tag_name')
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = u'mt_tag'

class Entry(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'entry_id')
    allow_comments = models.IntegerField(null = True, blank = True, db_column = 'entry_allow_comments')
    allow_pings = models.IntegerField(null = True, blank = True, db_column = 'entry_allow_pings')
    atom_id = models.CharField(max_length = 765, blank = True, db_column = 'entry_atom_id')
    author = models.ForeignKey(Author, db_column = 'entry_author_id')
    authored_on = models.DateTimeField(null = True, blank = True, db_column = 'entry_authored_on')
    basename = models.CharField(max_length = 765, blank = True, db_column = 'entry_basename')
    blog = models.ForeignKey(Blog, db_column = 'entry_blog_id', related_name='entries')
    category = models.ForeignKey(Category, null = True, blank = True, db_column = 'entry_category_id')
    categories = models.ManyToManyField(Category, related_name='entries', through='Placement')
    class_field = models.CharField(max_length = 765, blank = True, db_column = 'entry_class')
    comment_count = models.IntegerField(null = True, blank = True, db_column = 'entry_comment_count')
    convert_breaks = models.CharField(max_length = 90, blank = True, db_column = 'entry_convert_breaks')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'entry_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'entry_created_on')
    excerpt = models.TextField(blank = True, db_column = 'entry_excerpt')
    keywords = models.TextField(blank = True, db_column = 'entry_keywords')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'entry_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'entry_modified_on')
    ping_count = models.IntegerField(null = True, blank = True, db_column = 'entry_ping_count')
    pinged_urls = models.TextField(blank = True, db_column = 'entry_pinged_urls')
    status = models.IntegerField(db_column = 'entry_status')
    tags = models.ManyToManyField(Tag, related_name='entries', through='EntryTag')
    tangent_cache = models.TextField(blank = True, db_column = 'entry_tangent_cache')
    template = models.ForeignKey(Template, null = True, blank = True, db_column = 'entry_template_id')
    text = models.TextField(blank = True, db_column = 'entry_text')
    text_more = models.TextField(blank = True, db_column = 'entry_text_more')
    title = models.CharField(max_length = 765, blank = True, db_column = 'entry_title')
    to_ping_urls = models.TextField(blank = True, db_column = 'entry_to_ping_urls')
    week_number = models.IntegerField(null = True, blank = True, db_column = 'entry_week_number')
    def __unicode__(self):
        return self.title
    class Meta:
        db_table = u'mt_entry'


class EntryMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'entry_meta_entry_id')
    type_field = models.CharField(max_length = 225, db_column = 'entry_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'entry_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'entry_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'entry_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'entry_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'entry_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'entry_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'entry_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'entry_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'entry_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'entry_meta_vclob')
    class Meta:
        db_table = u'mt_entry_meta'

class Comment(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'comment_id')
    author = models.CharField(max_length = 300, blank = True, db_column = 'comment_author')
    blog = models.ForeignKey(Blog, db_column = 'comment_blog_id', related_name='comments')
    commenter_id = models.IntegerField(null = True, blank = True, db_column = 'comment_commenter_id')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'comment_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'comment_created_on')
    email = models.CharField(max_length = 225, blank = True, db_column = 'comment_email')
    entry = models.ForeignKey(Entry, db_column = 'comment_entry_id', related_name='comments')
    ip = models.CharField(max_length = 48, blank = True, db_column = 'comment_ip')
    junk_log = models.TextField(blank = True, db_column = 'comment_junk_log')
    junk_score = models.FloatField(null = True, blank = True, db_column = 'comment_junk_score')
    junk_status = models.IntegerField(null = True, blank = True, db_column = 'comment_junk_status')
    last_moved_on = models.DateTimeField(db_column = 'comment_last_moved_on')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'comment_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'comment_modified_on')
    parent = models.ForeignKey('self', null = True, blank = True, db_column = 'comment_parent_id', related_name='children')
    text = models.TextField(blank = True, db_column = 'comment_text')
    url = models.CharField(max_length = 765, blank = True, db_column = 'comment_url')
    visible = models.IntegerField(null = True, blank = True, db_column = 'comment_visible')
    class Meta:
        db_table = u'mt_comment'
    class Admin:
        pass

class CommentMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'comment_meta_comment_id')
    type_field = models.CharField(max_length = 225, db_column = 'comment_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'comment_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'comment_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'comment_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'comment_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'comment_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'comment_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'comment_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'comment_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'comment_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'comment_meta_vclob')
    class Meta:
        db_table = u'mt_comment_meta'

class Config(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'config_id')
    data = models.TextField(blank = True, db_column = 'config_data')
    class Meta:
        db_table = u'mt_config'

class Field(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'field_id')
    basename = models.CharField(max_length = 765, blank = True, db_column = 'field_basename')
    blog = models.ForeignKey(Blog, null = True, blank = True, db_column = 'field_blog_id', related_name='fields')
    default = models.TextField(blank = True, db_column = 'field_default')
    description = models.TextField(blank = True, db_column = 'field_description')
    name = models.CharField(max_length = 765, db_column = 'field_name')
    obj_type = models.CharField(max_length = 150, db_column = 'field_obj_type')
    options = models.TextField(blank = True, db_column = 'field_options')
    required = models.IntegerField(null = True, blank = True, db_column = 'field_required')
    tag = models.CharField(max_length = 765, db_column = 'field_tag')
    type_field = models.CharField(max_length = 150, db_column = 'field_type')
    class Meta:
        db_table = u'mt_field'

class FileInfo(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'fileinfo_id')
    archive_type = models.CharField(max_length = 765, blank = True, db_column = 'fileinfo_archive_type')
    author = models.ForeignKey(Author, null = True, blank = True, db_column = 'fileinfo_author_id')
    blog = models.ForeignKey(Blog, db_column = 'fileinfo_blog_id', related_name='files')
    category = models.ForeignKey(Category, null = True, blank = True, db_column = 'fileinfo_category_id', related_name='files')
    entry = models.ForeignKey(Entry, null = True, blank = True, db_column = 'fileinfo_entry_id', related_name='files')
    file_path = models.TextField(blank = True, db_column = 'fileinfo_file_path')
    startdate = models.CharField(max_length = 240, blank = True, db_column = 'fileinfo_startdate')
    template = models.ForeignKey(Template, null = True, blank = True, db_column = 'fileinfo_template_id', related_name='files')
    templatemap = models.ForeignKey(TemplateMap, null = True, blank = True, db_column = 'fileinfo_templatemap_id', related_name='files')
    url = models.CharField(max_length = 765, blank = True, db_column = 'fileinfo_url')
    virtual = models.IntegerField(null = True, blank = True, db_column = 'fileinfo_virtual')
    class Meta:
        db_table = u'mt_fileinfo'

class IpBanlist(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'ipbanlist_id')
    blog = models.ForeignKey(Blog, db_column = 'ipbanlist_blog_id', related_name='banlist')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'ipbanlist_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'ipbanlist_created_on')
    ip = models.CharField(max_length = 45, db_column = 'ipbanlist_ip')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'ipbanlist_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'ipbanlist_modified_on')
    class Meta:
        db_table = u'mt_ipbanlist'

class Log(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'log_id')
    author = models.ForeignKey(Author, null = True, blank = True, db_column = 'log_author_id')
    blog = models.ForeignKey(Blog, null = True, blank = True, db_column = 'log_blog_id', related_name='logs')
    category = models.CharField(max_length = 765, blank = True, db_column = 'log_category')
    class_field = models.CharField(max_length = 765, blank = True, db_column = 'log_class')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'log_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'log_created_on')
    ip = models.CharField(max_length = 48, blank = True, db_column = 'log_ip')
    level = models.IntegerField(null = True, blank = True, db_column = 'log_level')
    message = models.TextField(blank = True, db_column = 'log_message')
    metadata = models.CharField(max_length = 765, blank = True, db_column = 'log_metadata')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'log_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'log_modified_on')
    class Meta:
        db_table = u'mt_log'

class Notification(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'notification_id')
    blog = models.ForeignKey(Blog, db_column = 'notification_blog_id', related_name='notifications')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'notification_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'notification_created_on')
    email = models.CharField(max_length = 225, blank = True, db_column = 'notification_email')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'notification_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'notification_modified_on')
    name = models.CharField(max_length = 150, blank = True, db_column = 'notification_name')
    url = models.CharField(max_length = 765, blank = True, db_column = 'notification_url')
    class Meta:
        db_table = u'mt_notification'

class ObjectAsset(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'objectasset_id')
    asset = models.ForeignKey(Asset, db_column = 'objectasset_asset_id')
    blog = models.ForeignKey(Blog, null = True, blank = True, db_column = 'objectasset_blog_id')
    embedded = models.IntegerField(null = True, blank = True, db_column = 'objectasset_embedded')
    object_ds = models.CharField(max_length = 150, db_column = 'objectasset_object_ds')
    object_id = models.IntegerField(db_column = 'objectasset_object_id')
    class Meta:
        db_table = u'mt_objectasset'

class ObjectScore(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'objectscore_id')
    author = models.ForeignKey(Author, null = True, blank = True, db_column = 'objectscore_author_id')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'objectscore_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'objectscore_created_on')
    ip = models.CharField(max_length = 48, blank = True, db_column = 'objectscore_ip')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'objectscore_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'objectscore_modified_on')
    namespace = models.CharField(max_length = 765, db_column = 'objectscore_namespace')
    object_ds = models.CharField(max_length = 150, db_column = 'objectscore_object_ds')
    object_id = models.IntegerField(null = True, blank = True, db_column = 'objectscore_object_id')
    score = models.FloatField(null = True, blank = True, db_column = 'objectscore_score')
    class Meta:
        db_table = u'mt_objectscore'

"""
class ObjectTag(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'objecttag_id')
    blog = models.ForeignKey(Blog, null = True, blank = True, db_column = 'objecttag_blog_id')
    object_datasource = models.CharField(max_length = 150, db_column = 'objecttag_object_datasource')
    object_id = models.IntegerField(db_column = 'objecttag_object_id')
    tag = models.ForeignKey(Tag, db_column = 'objecttag_tag_id')
    class Meta:
        db_table = u'mt_objecttag'
"""

class EntryTag(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'objecttag_id')
    blog = models.ForeignKey(Blog, null = True, blank = True, db_column = 'objecttag_blog_id')
    object_datasource = models.CharField(max_length = 150, db_column = 'objecttag_object_datasource')
    entry = models.ForeignKey(Entry, db_column = 'objecttag_object_id')
    tag = models.ForeignKey(Tag, db_column = 'objecttag_tag_id')
    class Meta:
        db_table = u'mt_objecttag'

class Permission(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'permission_id')
    author = models.ForeignKey(Author, db_column = 'permission_author_id')
    blog = models.ForeignKey(Blog, db_column = 'permission_blog_id', related_name='permissions')
    blog_prefs = models.CharField(max_length = 765, blank = True, db_column = 'permission_blog_prefs')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'permission_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'permission_created_on')
    entry_prefs = models.TextField(blank = True, db_column = 'permission_entry_prefs')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'permission_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'permission_modified_on')
    permissions = models.TextField(blank = True, db_column = 'permission_permissions')
    restrictions = models.TextField(blank = True, db_column = 'permission_restrictions')
    role_mask = models.IntegerField(null = True, blank = True, db_column = 'permission_role_mask')
    template_prefs = models.CharField(max_length = 765, blank = True, db_column = 'permission_template_prefs')
    class Meta:
        db_table = u'mt_permission'

class Placement(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'placement_id')
    blog = models.ForeignKey(Blog, db_column = 'placement_blog_id', related_name='placements')
    category = models.ForeignKey(Category, db_column = 'placement_category_id', related_name='placements')
    entry = models.ForeignKey(Entry, db_column = 'placement_entry_id', related_name='placements')
    is_primary = models.IntegerField(db_column = 'placement_is_primary')
    class Meta:
        db_table = u'mt_placement'

class PluginData(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'plugindata_id')
    data = models.TextField(blank = True, db_column = 'plugindata_data')
    key = models.CharField(max_length = 765, db_column = 'plugindata_key')
    plugin = models.CharField(max_length = 150, db_column = 'plugindata_plugin')
    class Meta:
        db_table = u'mt_plugindata'

class ProfileEvent(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'profileevent_id')
    author = models.ForeignKey(Author, db_column = 'profileevent_author_id', related_name='events')
    class_field = models.CharField(max_length = 765, blank = True, db_column = 'profileevent_class')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'profileevent_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'profileevent_created_on')
    identifier = models.CharField(max_length = 600, blank = True, db_column = 'profileevent_identifier')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'profileevent_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'profileevent_modified_on')
    visible = models.IntegerField(db_column = 'profileevent_visible')
    class Meta:
        db_table = u'mt_profileevent'

class ProfileEventMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'profileevent_meta_profileevent_id')
    type_field = models.CharField(max_length = 225, db_column = 'profileevent_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'profileevent_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'profileevent_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'profileevent_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'profileevent_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'profileevent_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'profileevent_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'profileevent_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'profileevent_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'profileevent_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'profileevent_meta_vclob')
    class Meta:
        db_table = u'mt_profileevent_meta'

class Session(models.Model):
    id = models.CharField(max_length = 240, primary_key = True, db_column = 'session_id')
    data = models.TextField(blank = True, db_column = 'session_data')
    email = models.CharField(max_length = 765, blank = True, db_column = 'session_email')
    kind = models.CharField(max_length = 6, blank = True, db_column = 'session_kind')
    name = models.CharField(max_length = 765, blank = True, db_column = 'session_name')
    start = models.IntegerField(db_column = 'session_start')
    class Meta:
        db_table = u'mt_session'

class TbPing(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'tbping_id')
    blog = models.ForeignKey(Blog, db_column = 'tbping_blog_id', related_name='pings')
    blog_name = models.CharField(max_length = 765, blank = True, db_column = 'tbping_blog_name')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'tbping_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'tbping_created_on')
    excerpt = models.TextField(blank = True, db_column = 'tbping_excerpt')
    ip = models.CharField(max_length = 45, db_column = 'tbping_ip')
    junk_log = models.TextField(blank = True, db_column = 'tbping_junk_log')
    junk_score = models.FloatField(null = True, blank = True, db_column = 'tbping_junk_score')
    junk_status = models.IntegerField(db_column = 'tbping_junk_status')
    last_moved_on = models.DateTimeField(db_column = 'tbping_last_moved_on')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'tbping_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'tbping_modified_on')
    source_url = models.CharField(max_length = 765, blank = True, db_column = 'tbping_source_url')
    tb_id = models.IntegerField(db_column = 'tbping_tb_id')
    title = models.CharField(max_length = 765, blank = True, db_column = 'tbping_title')
    visible = models.IntegerField(null = True, blank = True, db_column = 'tbping_visible')
    class Meta:
        db_table = u'mt_tbping'

class TbPingMeta(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'tbping_meta_tbping_id')
    type_field = models.CharField(max_length = 225, db_column = 'tbping_meta_type')
    vchar = models.CharField(max_length = 765, blank = True, db_column = 'tbping_meta_vchar')
    vchar_idx = models.CharField(max_length = 765, blank = True, db_column = 'tbping_meta_vchar_idx')
    vdatetime = models.DateTimeField(null = True, blank = True, db_column = 'tbping_meta_vdatetime')
    vdatetime_idx = models.DateTimeField(null = True, blank = True, db_column = 'tbping_meta_vdatetime_idx')
    vinteger = models.IntegerField(null = True, blank = True, db_column = 'tbping_meta_vinteger')
    vinteger_idx = models.IntegerField(null = True, blank = True, db_column = 'tbping_meta_vinteger_idx')
    vfloat = models.FloatField(null = True, blank = True, db_column = 'tbping_meta_vfloat')
    vfloat_idx = models.FloatField(null = True, blank = True, db_column = 'tbping_meta_vfloat_idx')
    vblob = models.TextField(blank = True, db_column = 'tbping_meta_vblob')
    vclob = models.TextField(blank = True, db_column = 'tbping_meta_vclob')
    class Meta:
        db_table = u'mt_tbping_meta'

class Touch(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'touch_id')
    blog = models.ForeignKey(Blog, null = True, blank = True, db_column = 'touch_blog_id', related_name='touches')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'touch_modified_on')
    object_type = models.CharField(max_length = 765, blank = True, db_column = 'touch_object_type')
    class Meta:
        db_table = u'mt_touch'

class Trackback(models.Model):
    id = models.IntegerField(primary_key = True, db_column = 'trackback_id')
    blog = models.ForeignKey(Blog, db_column = 'trackback_blog_id', related_name='trackbacks')
    category = models.ForeignKey(Category, db_column = 'trackback_category_id')
    created_by = models.IntegerField(null = True, blank = True, db_column = 'trackback_created_by')
    created_on = models.DateTimeField(null = True, blank = True, db_column = 'trackback_created_on')
    description = models.TextField(blank = True, db_column = 'trackback_description')
    entry = models.ForeignKey(Entry, db_column = 'trackback_entry_id', related_name='trackbacks')
    is_disabled = models.IntegerField(null = True, blank = True, db_column = 'trackback_is_disabled')
    modified_by = models.IntegerField(null = True, blank = True, db_column = 'trackback_modified_by')
    modified_on = models.DateTimeField(null = True, blank = True, db_column = 'trackback_modified_on')
    passphrase = models.CharField(max_length = 90, blank = True, db_column = 'trackback_passphrase')
    rss_file = models.CharField(max_length = 765, blank = True, db_column = 'trackback_rss_file')
    title = models.CharField(max_length = 765, blank = True, db_column = 'trackback_title')
    url = models.CharField(max_length = 765, blank = True, db_column = 'trackback_url')
    class Meta:
        db_table = u'mt_trackback'

class TsError(models.Model):
    time = models.IntegerField(primary_key = True, db_column = 'ts_error_error_time')
    funcid = models.IntegerField(db_column = 'ts_error_funcid')
    jobid = models.IntegerField(db_column = 'ts_error_jobid')
    message = models.CharField(max_length = 765, db_column = 'ts_error_message')
    class Meta:
        db_table = u'mt_ts_error'

class TsExitStatus(models.Model):
    jobid = models.IntegerField(primary_key = True, db_column = 'ts_exitstatus_jobid')
    completion_time = models.IntegerField(null = True, blank = True, db_column = 'ts_exitstatus_completion_time')
    delete_after = models.IntegerField(null = True, blank = True, db_column = 'ts_exitstatus_delete_after')
    funcid = models.IntegerField(db_column = 'ts_exitstatus_funcid')
    status = models.IntegerField(null = True, blank = True, db_column = 'ts_exitstatus_status')
    class Meta:
        db_table = u'mt_ts_exitstatus'

class TsFuncMap(models.Model):
    funcid = models.IntegerField(primary_key = True, db_column = 'ts_funcmap_funcid')
    funcname = models.CharField(unique = True, max_length = 765, db_column = 'ts_funcmap_funcname')
    class Meta:
        db_table = u'mt_ts_funcmap'

class TsJob(models.Model):
    jobid = models.IntegerField(primary_key = True, db_column = 'ts_job_jobid')
    arg = models.TextField(blank = True, db_column = 'ts_job_arg')
    coalesce = models.CharField(max_length = 765, blank = True, db_column = 'ts_job_coalesce')
    funcid = models.IntegerField(db_column = 'ts_job_funcid')
    grabbed_until = models.IntegerField(db_column = 'ts_job_grabbed_until')
    insert_time = models.IntegerField(null = True, blank = True, db_column = 'ts_job_insert_time')
    priority = models.IntegerField(null = True, blank = True, db_column = 'ts_job_priority')
    run_after = models.IntegerField(db_column = 'ts_job_run_after')
    uniqkey = models.CharField(unique = True, max_length = 765, blank = True, db_column = 'ts_job_uniqkey')
    class Meta:
        db_table = u'mt_ts_job'


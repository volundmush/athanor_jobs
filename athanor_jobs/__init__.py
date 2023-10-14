def init(settings, plugins):
    settings.BASE_BUCKET_TYPECLASS = "athanor.jobs.jobs.DefaultBucket"
    settings.INSTALLED_APPS.append("athanor_jobs")
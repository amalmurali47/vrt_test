# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/)

## [Unreleased]
### Added

### Removed

### Changed

## [v1.10.1](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.10...v1.10.1) - 2021-03-29
### Changed
- renamed `secure code warriors` mapping to `secure code warrior`

## [v1.10](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.9...v1.10) - 2021-03-18
### Added
- insufficient_security_configurability.verification_of_contact_method_not_required
- insufficient_security_configurability.weak_two_fa_implementation.two_fa_code_is_not_updated_after_new_code_is_requested
- insufficient_security_configurability.weak_two_fa_implementation.old_two_fa_code_is_not_invalidated_after_new_code_is_generated
- broken_authentication_and_session_management.weak_login_function.over_http
- server_security_misconfiguration.oauth_misconfiguration.account_squatting
- Third-party mapping to [Secure Code Warrior](https://www.securecodewarrior.com/) trainings
- automotive_security_misconfiguration.can.injection_battery_management_system
- automotive_security_misconfiguration.can.injection_steering_control
- automotive_security_misconfiguration.can.injection_pyrotechnical_device_deployment_tool
- automotive_security_misconfiguration.can.injection_headlights
- automotive_security_misconfiguration.can.injection_sensors
- automotive_security_misconfiguration.can.injection_vehicle_anti_theft_systems
- automotive_security_misconfiguration.can.injection_powertrain
- automotive_security_misconfiguration.can.injection_basic_safety_message
- automotive_security_misconfiguration.battery_management_system
- automotive_security_misconfiguration.battery_management_system.firmware_dump
- automotive_security_misconfiguration.battery_management_system.fraudulent_interface
- automotive_security_misconfiguration.gnss_gps
- automotive_security_misconfiguration.gnss_gps.spoofing
- automotive_security_misconfiguration.immobilizer
- automotive_security_misconfiguration.immobilizer.engine_start
- automotive_security_misconfiguration.abs
- automotive_security_misconfiguration.abs.unintended_acceleration_brake
- automotive_security_misconfiguration.rsu
- automotive_security_misconfiguration.rsu.sybil_attack
- automotive_security_misconfiguration.infotainment_radio_head_unit
- automotive_security_misconfiguration.infotainment_radio_head_unit.pii_leakage
- automotive_security_misconfiguration.infotainment_radio_head_unit.ota_firmware_manipulation
- automotive_security_misconfiguration.infotainment_radio_head_unit.code_execution_can_bus_pivot
- automotive_security_misconfiguration.infotainment_radio_head_unit.code_execution_no_can_bus_pivot
- automotive_security_misconfiguration.infotainment_radio_head_unit.unauthorized_access_to_services
- automotive_security_misconfiguration.infotainment_radio_head_unit.source_code_dump
- automotive_security_misconfiguration.infotainment_radio_head_unit.dos_brick
- automotive_security_misconfiguration.infotainment_radio_head_unit.default_credentials

### Removed
- insufficient_security_configurability.lack_of_verification_email
- broken_authentication_and_session_management.weak_login_function.https_not_available_or_http_by_default
- broken_authentication_and_session_management.weak_login_function.http_and_https_available
- broken_authentication_and_session_management.weak_login_function.lan_only
- cross_site_request_forgery_csrf.flash_based.high_impact
- cross_site_request_forgery_csrf.flash_based.low_impact
- automotive_security_misconfiguration.infotainment
- automotive_security_misconfiguration.infotainment.pii_leakage
- automotive_security_misconfiguration.infotainment.code_execution_can_bus_pivot
- automotive_security_misconfiguration.infotainment.code_execution_no_can_bus_pivot
- automotive_security_misconfiguration.infotainment.unauthorized_access_to_services
- automotive_security_misconfiguration.infotainment.source_code_dump
- automotive_security_misconfiguration.infotainment.dos_brick
- automotive_security_misconfiguration.infotainment.default_credentials

### Changed
 - server_security_misconfiguration.lack_of_security_headers.cache_control_for_a_non_sensitive_page updated remediation advice
 - server_security_misconfiguration.lack_of_security_headers.cache_control_for_a_sensitive_page updated remediation advice
 - cross_site_scripting_xss.flash_based priority changed from P4 to P5
 - cross_site_request_forgery_csrf.flash_based priority changed from null to P5 (due to children removal)
 - using_components_with_known_vulnerabilities.rosetta_flash priority changed from P4 to P5

## [v1.9](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.8...v1.9) - 2020-05-22
### Added
- sensitive_data_exposure.disclosure_of_secrets.for_publicly_accessible_asset
- sensitive_data_exposure.disclosure_of_secrets.for_internal_asset
- sensitive_data_exposure.disclosure_of_secrets.pay_per_use_abuse
- sensitive_data_exposure.disclosure_of_secrets.intentionally_public_sample_or_invalid
- sensitive_data_exposure.disclosure_of_secrets.data_traffic_spam
- sensitive_data_exposure.disclosure_of_secrets.non_corporate_user
- server_side_injection.ssti.basic
- server_side_injection.ssti.custom
- sensitive_data_exposure.via_localstorage_sessionstorage.sensitive_token
- sensitive_data_exposure.via_localstorage_sessionstorage.non_sensitive_token
- mobile_security_misconfiguration.auto_backup_allowed_by_default
- server_security_misconfiguration.no_rate_limiting_on_form.change_password
- server_side_injection.content_spoofing.impersonation_via_broken_link_hijacking
- cross_site_request_forgery_csrf.flash_based.high_impact
- cross_site_request_forgery_csrf.flash_based.low_impact
- insufficient_security_configurability.password_policy_bypass

### Removed
- sensitive_data_exposure.critically_sensitive_data.password_disclosure
- sensitive_data_exposure.critically_sensitive_data.private_api_keys
- sensitive_data_exposure.critically_sensitive_data


## [v1.8](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.7.1...v1.8) - 2019-09-25
### Added
- server_security_misconfiguration.race_condition
- server_security_misconfiguration.cache_poisoning
- indicators_of_compromise
- broken_authentication_and_session_management.failure_to_invalidate_session.on_two_fa_activation_change

### Removed
- mobile_security_misconfiguration.clipboard_enabled.on_sensitive_content
- mobile_security_misconfiguration.clipboard_enabled.on_non_sensitive_content

### Changed
- server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_on_non_email_domain name changed from "Email Spoofing on non-email domain" to "Email Spoofing on Non-Email Domain"
- mobile_security_misconfiguration.clipboard_enabled priority changed from null to P5 (due to children removal)

##  [v1.7.1](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.7...v1.7.1) - 2019-04-15
### Added
- Remediation Advice and CVSS mappings for automotive_security_misconfiguration

##  [v1.7](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.6...v1.7) - 2019-03-13
### Added
- sensitive_data_exposure.weak_password_reset_implementation.token_leakage_via_host_header_poisoning
- server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_on_non_email_domain
- broken_access_control.username_enumeration.non_brute_force
- insufficient_security_configurability.weak_two_fa_implementation.two_fa_secret_cannot_be_rotated
- insufficient_security_configurability.weak_two_fa_implementation.two_fa_secret_remains_obtainable_after_two_fa_is_enabled
- insufficient_security_configurability.weak_two_fa_implementation
- sensitive_data_exposure.token_leakage_via_referer.trusted_third_party
- sensitive_data_exposure.token_leakage_via_referer.untrusted_third_party
- cross_site_scripting_xss.ie_only.ie_eleven
- cross_site_scripting_xss.ie_only.older_version_ie_eleven
- automotive_security_misconfiguration
- automotive_security_misconfiguration.infotainment
- automotive_security_misconfiguration.infotainment.pii_leakage
- automotive_security_misconfiguration.infotainment.code_execution_can_bus_pivot
- automotive_security_misconfiguration.infotainment.code_execution_no_can_bus_pivot
- automotive_security_misconfiguration.infotainment.unauthorized_access_to_services
- automotive_security_misconfiguration.infotainment.source_code_dump
- automotive_security_misconfiguration.infotainment.dos_brick
- automotive_security_misconfiguration.infotainment.default_credentials
- automotive_security_misconfiguration.rf_hub
- automotive_security_misconfiguration.rf_hub.key_fob_cloning
- automotive_security_misconfiguration.rf_hub.can_injection_interaction
- automotive_security_misconfiguration.rf_hub.data_leakage_pull_encryption_mechanism
- automotive_security_misconfiguration.rf_hub.unauthorized_access_turn_on
- automotive_security_misconfiguration.rf_hub.roll_jam
- automotive_security_misconfiguration.rf_hub.replay
- automotive_security_misconfiguration.rf_hub.relay
- automotive_security_misconfiguration.can
- automotive_security_misconfiguration.can.injection_disallowed_messages
- automotive_security_misconfiguration.can.injection_dos
- server_side_injection.content_spoofing.email_hyperlink_injection_based_on_email_provider

### Removed
- broken_access_control.username_enumeration.data_leak
- insufficient_security_configurability.weak_2fa_implementation
- sensitive_data_exposure.token_leakage_via_referer.trusted_3rd_party
- sensitive_data_exposure.token_leakage_via_referer.untrusted_3rd_party
- cross_site_scripting_xss.ie_only.ie11
- cross_site_scripting_xss.ie_only.older_version_ie11

### Changed
- server_security_misconfiguration.username_enumeration name changed from "Username Enumeration" to "Username/Email Enumeration"
- broken_access_control.username_enumeration name changed from "Username Enumeration" to "Username/Email Enumeration"
- updated Remediation Advice reference URLs for OWASP

## [v1.6](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.5...v1.6) - 2018-09-13
### Added
- broken_access_control.server_side_request_forgery_ssrf.internal_high_impact
- broken_access_control.server_side_request_forgery_ssrf.internal_scan_and_or_medium_impact
- server_security_misconfiguration.mail_server_misconfiguration.no_spoofing_protection_on_email_domain
- server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_to_inbox_due_to_missing_or_misconfigured_dmarc_on_email_domain
- server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_to_spam_folder
- server_security_misconfiguration.mail_server_misconfiguration.missing_or_misconfigured_spf_and_or_dkim

### Removed
- broken_access_control.server_side_request_forgery_ssrf.internal
- server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_on_email_domain
- server_security_misconfiguration.mail_server_misconfiguration.missing_spf_on_non_email_domain
- server_security_misconfiguration.mail_server_misconfiguration.spf_uses_a_soft_fail
- server_security_misconfiguration.mail_server_misconfiguration.spf_includes_10_lookups
- server_security_misconfiguration.mail_server_misconfiguration.missing_dmarc

## [v1.5](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.4...v1.5) - 2018-09-13
### Added
- unvalidated_redirects_and_forwards.open_redirect.flash_based
- cross_site_scripting_xss.flash_based
- server_side_injection.content_spoofing.flash_based_external_authentication_injection
- broken_authentication_and_session_management.session_fixation.remote_attack_vector
- broken_authentication_and_session_management.session_fixation.local_attack_vector
- broken_authentication_and_session_management.cleartext_transmission_of_session_token
- broken_access_control.server_side_request_forgery_ssrf.dns_query_only
- mobile_security_misconfiguration.clipboard_enabled
- mobile_security_misconfiguration.clipboard_enabled.on_sensitive_content
- mobile_security_misconfiguration.clipboard_enabled.on_non_sensitive_content
- server_security_misconfiguration.waf_bypass.direct_server_access
- broken_authentication_and_session_management.two_fa_bypass
- server_security_misconfiguration.no_rate_limiting_on_form.sms_triggering
- server_security_misconfiguration.mail_server_misconfiguration.email_spoofing_on_email_domain
- server_security_misconfiguration.insecure_ssl.certificate_error
- cross_site_scripting_xss.stored.privileged_user_to_privilege_elevation
- cross_site_scripting_xss.stored.privileged_user_to_no_privilege_elevation
- server_security_misconfiguration.clickjacking.form_input
- server_security_misconfiguration.misconfigured_dns.basic_subdomain_takeover
- server_security_misconfiguration.misconfigured_dns.high_impact_subdomain_takeover
- server_security_misconfiguration.captcha
- server_security_misconfiguration.captcha.missing
- cross_site_request_forgery_csrf.csrf_token_not_unique_per_request

### Removed
- server_security_misconfiguration.mail_server_misconfiguration.missing_spf_on_email_domain
- server_security_misconfiguration.mail_server_misconfiguration.email_spoofable_via_third_party_api_misconfiguration
- cross_site_scripting_xss.stored.admin_to_anyone
- server_security_misconfiguration.misconfigured_dns.subdomain_takeover
- server_security_misconfiguration.captcha_bypass

### Changed
- broken_authentication_and_session_management.failure_to_invalidate_session.on_password_change updated remediation advice
- CWE mapping default changed from `[CWE-2000]` to `null`
- Updated python version to 3.6
- cross_site_scripting_xss.stored.non_admin_to_anyone name changed from "Non-Admin to Anyone" to "Non-Privileged User to Anyone"
- server_security_misconfiguration.clickjacking.sensitive_action name changed from "Sensitive Action" to "Sensitive Click-Based Action"
- server_security_misconfiguration.captcha_bypass.implementation_vulnerability moved via subcategory change to server_security_misconfiguration.captcha.implementation_vulnerability
- server_security_misconfiguration.captcha_bypass.brute_force moved via subcategory change to server_security_misconfiguration.captcha.brute_force

## [v1.4](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.3.1...v1.4) - 2018-04-13
### Added
- insufficient_security_configurability.weak_password_reset_implementation.token_is_not_invalidated_after_login
- server_side_injection.content_spoofing.rtlo
- mapping of VRT to CWE
- server_security_misconfiguration.dbms_misconfiguration.excessively_privileged_user_dba
- cross_site_scripting_xss.stored.url_based
- server_security_misconfiguration.oauth_misconfiguration.insecure_redirect_uri
- server_security_misconfiguration.oauth_misconfiguration.account_takeover
- client_side_injection.binary_planting.non_default_folder_privilege_escalation
- broken_authentication_and_session_management.weak_login_function.not_operational
- broken_authentication_and_session_management.weak_login_function.other_plaintext_protocol_no_secure_alternative
- broken_authentication_and_session_management.weak_login_function.lan_only
- broken_authentication_and_session_management.weak_login_function.http_and_https_available
- broken_authentication_and_session_management.weak_login_function.https_not_available_or_http_by_default
- cross_site_scripting_xss.ie_only.ie11
- cross_site_scripting_xss.ie_only.older_version_ie11
- broken_authentication_and_session_management.failure_to_invalidate_session.on_logout_server_side_only
- sensitive_data_exposure.sensitive_token_in_url.user_facing
- sensitive_data_exposure.sensitive_token_in_url.in_the_background
- sensitive_data_exposure.sensitive_token_in_url.on_password_reset
- mapping of VRT to Remediation Advice

### Removed
- server_side_injection.sql_injection.error_based
- server_side_injection.sql_injection.blind
- broken_authentication_and_session_management.weak_login_function.over_http
- cross_site_scripting_xss.ie_only.older_version_ie_10_11
- cross_site_scripting_xss.ie_only.older_version_ie10
- broken_authentication_and_session_management.failure_to_invalidate_session.on_password_reset
- network_security_misconfiguration.telnet_enabled.credentials_required
- server_security_misconfiguration.using_default_credentials.production_server
- server_security_misconfiguration.using_default_credentials.staging_development_server

### Changed
- Use unittest for vrt validations
- broken_authentication_and_session_management.failure_to_invalidate_session.all_sessions name changed from "All Sessions" to "Concurrent Sessions On Logout"
- server_security_misconfiguration.oauth_misconfiguration.missing_state_parameter name changed from "Missing State Parameter" to "Missing/Broken State Parameter"
- server_security_misconfiguration.oauth_misconfiguration.missing_state_parameter priority changed from P4 to null
- server_security_misconfiguration.no_rate_limiting_on_form.login priority changed from P3 to P4
- client_side_injection.binary_planting.privilege_escalation name changed from "Privilege Escalation" to "Default Folder Privilege Escalation" priority changed from P4 to P3
- server_security_misconfiguration.lack_of_password_confirmation.change_email_address priority changed from P4 to P5
- server_security_misconfiguration.lack_of_password_confirmation.change_password priority changed from P4 to P5
- server_security_misconfiguration.unsafe_file_upload.no_antivirus priority changed from P4 to P5
- server_security_misconfiguration.unsafe_file_upload.no_size_limit priority changed from P4 to P5
- broken_authentication_and_session_management.failure_to_invalidate_session.on_logout name changed from "On Logout" to "On Logout (Client and Server-Side)"
- broken_authentication_and_session_management.failure_to_invalidate_session.on_password_change name changed from "On Password Change" to "On Password Reset and/or Change"
- network_security_misconfiguration.telnet_enabled priority changed from null to P5 (due to children removal)
- server_security_misconfiguration.using_default_credentials priority changed from null to P1 (due to children removal)

## [v1.3.1](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.3...v1.3.1) - 2017-10-31
### Changed
- references to the invalid insufficient_security_configurability.weak_password_policy.no_password_policy updated to insufficient_security_configurability.no_password_policy

## [v1.3.0](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.2...v1.3) - 2017-09-22
### Added
- insecure_data_transport.cleartext_transmission_of_sensitive_data
- broken_access_control
- broken_access_control.idor
- mobile_security_misconfiguration.tapjacking
- server_security_misconfiguration.misconfigured_dns.missing_caa_record
- mapping of VRT to CVSS V3
- server_security_misconfiguration.bitsquatting

### Removed
- missing_function_level_access_control
- insecure_direct_object_references_idor

### Changed
- missing_function_level_access_control.server_side_request_forgery_ssrf moved via category change to broken_access_control.server_side_request_forgery_ssrf
- missing_function_level_access_control.server_side_request_forgery_ssrf.internal moved via category change to broken_access_control.server_side_request_forgery_ssrf.internal
- missing_function_level_access_control.server_side_request_forgery_ssrf.external moved via category change to broken_access_control.server_side_request_forgery_ssrf.external
- missing_function_level_access_control.username_enumeration moved via category change to broken_access_control.username_enumeration
- missing_function_level_access_control.username_enumeration.data_leak moved via category change to broken_access_control.username_enumeration.data_leak
- missing_function_level_access_control.exposed_sensitive_android_intent moved via category change to broken_access_control.exposed_sensitive_android_intent
- missing_function_level_access_control.exposed_sensitive_ios_url_scheme moved via category change to broken_access_control.exposed_sensitive_ios_url_scheme
- cross_site_request_forgery_csrf.application_wide name changed from Applicaton-Wide to Application-Wide

## [v1.2.0](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.1...v1.2) - 2017-08-04
### Added
- sensitive_data_exposure.visible_detailed_error_page.descriptive_stack_trace
- sensitive_data_exposure.visible_detailed_error_page.detailed_server_configuration
- unvalidated_redirects_and_forwards.open_redirect.get_based
- sensitive_data_exposure.internal_ip_disclosure
- sensitive_data_exposure.visible_detailed_error_page.full_path_disclosure
- server_security_misconfiguration.cookie_scoped_to_parent_domain
- client_side_injection.binary_planting
- client_side_injection.binary_planting.privilege_escalation
- client_side_injection.binary_planting.no_privilege_escalation
- sensitive_data_exposure.token_leakage_via_referer.trusted_3rd_party
- sensitive_data_exposure.token_leakage_via_referer.untrusted_3rd_party
- server_security_misconfiguration.fingerprinting_banner_disclosure
- server_security_misconfiguration.lack_of_password_confirmation.manage_two_fa
- sensitive_data_exposure.json_hijacking
- cross_site_request_forgery_csrf.action_specific.logout
- broken_authentication_and_session_management.privilege_escalation
- insecure_data_transport.executable_download
- insecure_data_transport.executable_download.no_secure_integrity_check
- insecure_data_transport.executable_download.secure_integrity_check
- server_security_misconfiguration.rfd
- sensitive_data_exposure.xssi
- server_security_misconfiguration.misconfigured_dns.zone_transfer
- insufficient_security_configurability.no_password_policy (changelog text corrected in v1.4.0 #100)
- insecure_data_storage.server_side_credentials_storage
- insecure_data_storage.server_side_credentials_storage.plaintext

### Removed
- unvalidated_redirects_and_forwards.open_redirect.get_based_all_users
- unvalidated_redirects_and_forwards.open_redirect.get_based_authenticated
- unvalidated_redirects_and_forwards.open_redirect.get_based_unauthenticated
- sensitive_data_exposure.token_leakage_via_referer.over_https
- sensitive_data_exposure.mixed_content.sensitive_data_disclosure
- sensitive_data_exposure.mixed_content.requires_being_a_man_in_the_middle
- broken_authentication_and_session_management.session_token_in_url
- broken_authentication_and_session_management.session_token_in_url.over_http
- broken_authentication_and_session_management.session_token_in_url.over_https
- broken_authentication_and_session_management.authentication_bypass.vertical
- broken_authentication_and_session_management.authentication_bypass.horizontal
- insecure_data_storage.credentials_stored_unencrypted
- insecure_data_storage.credentials_stored_unencrypted.on_external_storage
- insecure_data_storage.credentials_stored_unencrypted.on_internal_storage
- insecure_data_storage.insecure_data_storage
- insecure_data_storage.insecure_data_storage.password
- insufficient_security_configurability.weak_password_policy.complexity_both_length_and_char_type_not_enforced
- insufficient_security_configurability.weak_password_policy.complexity_length_not_enforced
- insufficient_security_configurability.weak_password_policy.complexity_char_type_not_enforced
- insufficient_security_configurability.weak_password_policy.allows_reuse_of_old_passwords
- insufficient_security_configurability.weak_password_policy.allows_password_to_be_same_as_email_username

### Changed
- sensitive_data_exposure.visible_detailed_error_page name changed from 'Visible Detailed Error Page' to 'Visible Detailed Error/Debug Page'
- server_security_misconfiguration.mail_server_misconfiguration.missing_dmarc name changed from 'Missing DMARC' to 'Missing DKIM/DMARC'
- insecure_data_transport.ssl_certificate_pinning moved via category change to mobile_security_misconfiguration.ssl_certificate_pinning
- insecure_data_transport.ssl_certificate_pinning.absent moved via category change to mobile_security_misconfiguration.ssl_certificate_pinning.absent
- insecure_data_transport.ssl_certificate_pinning.defeatable moved via category change to mobile_security_misconfiguration.ssl_certificate_pinning.defeatable
- sensitive_data_exposure.mixed_content name changed from 'Mixed Content' to 'Mixed Content (HTTPS Sourcing HTTP)'
- sensitive_data_exposure.mixed_content priority changed from null to P5 (due to children removal)
- broken_authentication_and_session_management.authentication_bypass priority changed from null to P1 (due to children removal)
- insufficient_security_configurability.weak_password_policy priority changed from null to P5 (due to children removal)

## [v1.1.0](https://github.com/bugcrowd/vulnerability-rating-taxonomy/compare/v1.0...v1.1) - 2017-04-13
### Added
- directory_listing_enabled
- directory_listing_enabled.sensitive_data_exposure
- directory_listing_enabled.non_sensitive_data_exposure
- server_security_misconfiguration.path_traversal
- cross_site_scripting_xss.reflected.self
- cross_site_scripting_xss.reflected.non_self
- cross_site_request_forgery_csrf.application_wide
- cross_site_request_forgery_csrf.application_specific
- cross_site_request_forgery_csrf.authenticated_action
- cross_site_request_forgery_csrf.unauthenticated_action

### Removed
- poor_physical_security
- social_engineering

### Changed
- cross_site_scripting_xss.cookie_based priority changed from P4 to P5

## [1.0.0] - 2017-03-06

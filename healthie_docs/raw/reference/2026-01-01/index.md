---
title: Schema Reference | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/index
  md: https://docs.gethealthie.com/reference/2026-01-01/index.md
---

## Queries

`advanceAppointmentPrices`

Fetch paginated advance appointment prices collection

`allergySuggestions`

Search results for allergies, allergens, and reactions

`announcement`

Fetch an announcement

`announcements`

Fetch an array of announcements for a provider

`apiKeys`

Fetch paginated API Keys collection

`appliedTag`

An applied tag to a user

`appliedTags`

Fetch paginated applied tags collection

`appointment`

fetch an appointment by id, group appointments are (considered public)

`appointmentBookingWarnings`

Return potential booking issues for an appointment, date, time, repeats, attendees, and provider.

`appointmentFrequencyData`

returns metadata about appointments for provider dashboard

`appointmentInclusion`

fetch an appointment by id, group appointments are (considered public)

`appointmentLocation`

fetch an appointment location by id (considered public)

`appointmentLocations`

Fetch paginated appointment locations collection

`appointmentNumberPerDayOfMonth`

Returns a json hash of the number of appointments in each day of the month. The month is the month that the passed day is in.

`appointmentRequest`

Fetch a single appointment requests for a provider or organization

`appointmentRequests`

Fetch a collection of appointment requests for a provider or organization

`appointmentSetting`

fetch a Appointment Setting by id (considered public)

`appointmentType`

fetch an appointment type by id (considered public)

`appointmentTypeCreditChanges`

Fetch paginated appointment type credit changes collection

`appointmentTypes`

Fetch paginated Appointment Type collection (considered public)

`appointmentWorkflowStatuses`

Fetch paginated appointment workflow statuses collection

`appointments`

Fetch paginated appointment collection

`appointmentsSummary`

Data summary for appointment reports

`assumedBrand`

Get the assumed brand for the current user

`auditLog`

Fetch paginated Audit Log collection

`autoTaskGenerators`

Fetch paginated auto task generators collection

`automatedInsuranceBillingSetting`

fetch the automated insurance billing setting

`availabilities`

Fetch availabilities for range

`availability`

Fetch availability

`availabilitySummaryJson`

(Limited availability, subject to breaking changes). JSONified Hash with summary of availability.

`availableItemTypes`

Fetch available item types (for use in onboarding items)

`availableSlotsForRange`

Get open appointment times for a date range. Returns array of dates sorted in ascending order (considered public)

`baseCms1500ForUser`

Get the Cms1500 Policies object for a given claim and client

`basicUserInfoFromToken`

Get basic info about User from signup token

`billableIcdCodes` deprecated

DEPRECATED: All ICD Codes that are allowed to be used in healthcare claims

`billingItem`

fetch a billing item by id

`billingItems`

Fetch paginated Billing Items collection

`brand`

fetch a Brand by id (considered public)

`brandFromCustomSignInPath`

fetch a Brand by custom sign in path (considered public)

`brandInfo`

get info used on authentication pages for either a dietitian or partner

`calendarViewSetting`

Fetch a calendar view settings for current user

`canCapOfferingPurchases`

Check if the user has access to the package buy limit feature

`canInvoiceSenderSeeRecipient`

Check if provider has access to client

`candidHealthConnection`

fetch the current users candidhealth connection

`cardIssues`

Fetch paginated stripe customer accounts with associated errors or soon to expire credit cards

`carePlan`

fetch a single care plan

`carePlans`

Fetch paginated care plan collection

`cdaActivityEvents`

Fetch paginated CDA activity events collection

`changeClaimSubmitter`

fetch the current users Change Health connection

`chargeBack`

fetch a chargeback by the Healthie ID or the Stripe Dispute ID.

`chargeBacks`

fetch all charge backs for a user or organization

`chargeDisputes`

Fetch Stripe Charge Disputes for an organization

`chartNotes`

Load all charting notes accessible by this user

`chartingItems`

All items to include in the charting list

`chartingNoteAddendum`

Fetch a charting note addendum by id

`chatSetting`

fetch a Chat Setting

`closeToCurrentVideoChats`

get current video chats for a user.

`cms1500`

Fetch a CMS1500 by ID

`cms1500s`

Fetch paginated Cms1500s collection

`colorCodeOptions`

Color Code Options for a given category

`comment`

Fetch comment

`comments`

Fetch comments collection

`completedCourseItem`

fetch a completedCourseItem by course\_item\_id and user\_id

`completedOnboardingItem`

Get the completed onboarding item by ID

`contactTypes`

All Contact Types For Current User

`conversation`

fetch a conversation by id

`conversationMembership`

fetch a conversation membership by id

`conversationMembershipInvitees`

Fetch paginated conversation membership invitees collection

`conversationMemberships`

Fetch paginated conversation memberships collection

`conversationMembershipsAllCounts`

All conversation membership tab counts in a single query

`conversations`

Fetch paginated conversations collection

`course`

fetch a course by id (considered public)

`courseClients`

fetch clients belonging to a course by course\_id

`courseCompletetionInfo` deprecated

Get course completion info for users and user\_groups

`courseCompletionInfo`

Get course completion info for users and user\_groups

`courseGroupClients`

Fetch paginated course group clients collection

`courseItem`

fetch a courseitem by id (considered public)

`courseItemCustomEmails`

Fetch paginated course item custom emails collection

`courseItemDocuments`

Fetch paginated course item documents collection

`courseItemForms`

Fetch paginated course item forms collection

`courseItems`

Fetch paginated course items collection

`courseMembership`

fetch a courseMembership by id

`courseMemberships`

Fetch paginated course membership collection

`courses`

Fetch paginated course collection

`cptCodes`

All CPT Codes

`currentUser`

fetch the current user.

`currentVideoChats`

get current video chats for a user.

`customEmail`

Custom Email object

`customEmailPreview`

A HTML string containing mailer template for certain email type

`customEmails`

Fetch paginated custom emails collection

`customModuleForm`

fetch a custom module form by ID (templates are considered public)

`customModuleForms`

All form templates for the current user

`customModuleFormsCount`

Fetch paginated count for provider custom module forms

`customModules`

Fetch paginated copied fields (is\_custom custom modules) for the current user

`daysAvailableForRange`

get open appointment times for a range (considered public)

`document`

fetch a document by id

`documentViewings`

Get Document Viewings for a specific document. A 'View' is when a document is downloaded or opened in a new tab

`documents`

Fetch paginated documents collection

`dosespotUserInfo`

Fetch User Info on DoseSpot Object

`dosespot_ui_link`

Fetch the iframe link to prescribe for a given patient (patient must have valid phone\_number, dob, location.line1, location.city, location.state, and location.zip)

`draft`

draft by conversation\_membership id

`drugAllergen`

Fetch an allergen by ID

`drugAllergens`

Search for allergens by name

`dsiComment`

Fetch DSI comment for given intervention\_type

`dynamicLink`

Fetch a link from Fullscript to create a treatment plan for a given user

`embedWidgetSteps`

fetch embed steps based off of params

`entries`

Fetch paginated entries collection

`entry`

fetch an entry by id

`episodesOfCare`

Fetch paginated episodes of care collection

`externalCalendars`

Fetch paginated external calendars collection

`featureToggle`

fetch a featureToggle by id

`featureToggleForEditing`

fetch a featureToggle by id

`folder`

fetch a folder by id

`folders`

Fetch paginated folders collection

`foodSearch`

Fetch food items

`formAnswerGroup`

Fetch a form answer group by id

`formAnswerGroups`

All filled forms for a given set of arguments

`formHistories`

Fetch paginated form histories collection

`formTypesToRequest`

Fetch available forms to request

`fullscriptPractitionerTypes`

Fullscript practitioners that share the same clinic id as organization owner

`fullscriptPractitioners`

Fullscript practitioners that share the same clinic id as organization owner

`goal`

fetch a goal by id

`goalHistories`

All completed goals for a given set of users

`goalHistory`

Fetch goal history

`goalInstances`

A goal's instances

`goalTemplates`

Fetch paginated goal templates collection

`goals`

All goals, either for a given user or for all of the providers clients

`goalsData`

All goals data

`goalsOverallCompletionRate` deprecated

Overall completion percentage of goals

`goalsOverallCompletionRateInfo`

Overall completion percentage of goals

`hasConditionalQuestionEditing`

When true, the user can set up question conditions in the form builder

`hasFormsToComplete`

Checks if the specified user has any forms to complete.

`hasSubLabels`

When true, the user can add sublabels to questions in the form builder

`healthAssessment` deprecated

DEPRECATED: Fetch a single health assessment

`healthAssessments`

Fetch Health Assessments

`icdCode`

Fetch ICD Code by ID

`icdCodes`

All ICD Codes

`importDataRequest`

fetch import data request by user\_id

`initialCms1500`

A new CMS1500 form with some objects already prefilled

`initialFormAnswers`

Initial form answers for a given user and template

`initialServiceDate`

Initial date of service for a new form answer group

`initializedOfferingIncludes`

appointment types related to offering

`insuranceAuthorization`

Insurance Authorization belonging to a client

`insurancePayments`

Fetch insurance payments for authenticated provider

`insurancePlans`

Get all potential insurance plans

`intakeFlow`

Fetch intake flow

`integrationsList`

Fetch paginated integrations list collection

`invoiceBasePrice`

get the base price for the invoice based off the associated item

`invoiceTemplates`

Fetch paginated invoice templates collection

`labFiltersData`

Get options for lab filters

`labOptions`

Fetch paginated lab options collection

`labOrder`

Fetch onboarding flows collection

`labOrders`

Fetch Lab Orders collection

`labResult`

Fetch a laboratory result by ID

`lastCM`

Fetch most recent conversationMembership

`lastClientActivities`

Fetch paginated last client activities collection

`loadMoreNotesCalled`

has loadMoreNotes been called

`location`

fetch a location by id

`locationResources`

Get location resources

`locations`

Get locations for a given user (or current user)

`mealSearch`

Fetch user meals

`meal_plan_options`

Meal plan options from user Living Plate account. Nil if no Living Plate account associated

`medication`

Fetch a medication by ID

`medication_option`

`medication_options`

Fetch an array of medications options. Considered Public

`medications`

Fetch paginated medications collection

`metricGraphData`

Fetch data for the metric graphs for a given user

`metricGraphsData`

Fetch data for the metric graphs for a given user

`minimumOfferingPrice`

`monthlyBillingItemsData`

returns metadata about monthly payments

`multiLineMetricGraphData`

Graph data with multiple data series for a single specified metric category

`newClientPriceString`

String containing info for the user about the client upgrade price

`newOrganizationPriceString`

String containing info for the user about the org upgrade price

`newOrganizationSupportPriceString`

String containing info for the user about the org upgrade price when adding a new support user

`nextAppointment`

Fetch closest appointment

`nextAvailableSlot`

get open appointment times for a range (considered public)

`nextCourseItem`

fetch a courseitem by id (considered public)

`note`

fetch a note by id

`noteViewedStatus`

get the viewed status of a note

`note_scheduler`

Fetch note scheduler by id

`notes`

Fetch paginated Note collection for given conversation

`notificationSetting`

fetch a Notification Setting by id

`notifications`

Get notifications for a given user (or for the current user)

`offering`

fetch an offering by id (considered public)

`offeringBillingItems`

Fetch paginated offering billing items collection

`offeringCoupons`

Fetch paginated coupon offerings collection

`offeringGroupVisibilities`

Fetch paginated offering group visibilities collection

`offeringImages`

Fetch paginated offering images collection

`offerings`

Fetch paginated offerings collection (considered public)

`offeringsData`

returns metadata about offerings purchased

`officeallySftpAccount`

fetch the current users officeally sftp connection

`onboardingFlow`

Fetch an onboarding flow by id or uuid

`onboardingFlows`

Fetch onboarding flows collection

`onboardingItem`

fetch an onboarding item by id (considered public)

`orgProvidersCptCodes`

Fetch paginated org providers CPT codes collection

`organization`

Fetch an organization by id, by provider id, or by the current\_user, demographic org info is (considered public)

`organizationCptCode`

Returns organization cpt code object

`organizationFeeScheduleCptCode`

Fetch CPT code and fee schedule pricing by CPT code ID

`organizationFeeScheduleCptCodes`

Provides CPT codes for an organization as configured in their fee schedule

`organizationInfo`

Fetch organization info by id

`organizationMembers`

fetch members of organization

`organizationMembership`

Get the organization membership info of the current user, basic org member info is (considered public)

`organizationMemberships`

Fetch paginated organization memberships collection

`otherIdNumber`

fetch an Other Id Number by id

`otherIdNumbers`

Fetch paginated other ID numbers collection

`paginate_transfers`

returns true if the there are more transfers to load

`patientEncounter`

Fetch a patient encounter

`payoutAccount`

Fetch a single payout account by ID

`payoutAccounts`

List all payout accounts for the current organization

`pdfLetterheadTemplate`

`pdfLetterheadTemplatePreview`

PDF Letterhead HTML String. Falls back to the system default template unless \`pdf\_letterhead\_template\_id\` is given

`permissionTemplate`

Fetch permission template

`permissionTemplates`

Get Permission Templates

`pharamcy` deprecated

Fetch a pharmacy given dosespot pharmacy id

`pharmacies`

Fetch an array of pharmacies given search parameters. One of zip, ncpdp\_id, or phone\_or\_fax is required

`pharmacy`

Fetch a pharmacy given dosespot pharmacy id

`placeOfServices`

Fetch paginated place of services collection

`plan`

fetch a Plan by id (considered public)

`policy`

fetch a policy by id

`preferred_medical_codes`

Fetch paginated preferred medical codes collection

`prescription`

Fetch a prescription for a given patient and prescription ID pulled from DoseSpot

`prescriptionMedications`

Fetches combined list of prescriptions and medications

`prescriptions` deprecated

Fetch an array of prescriptions for a given patient pulled from DoseSpot

`prevCourseItem`

fetch a courseitem by id (considered public)

`products`

Fetch paginated product collection

`provider`

fetch a provider by id

`providerAcceptedInsurancePlan`

Fetch a single accepted insurance plan for a provider

`providerAcceptedInsurancePlans`

Fetch paginated provider accepted insurance plans collection

`providerAppointmentLocations`

Fetch paginated provider appointment locations collection

`providerCptCodes`

Fetch paginated provider CPT codes collection

`questionBankModules`

Fetch generic custom modules for use in the form builder

`receiptLineItems`

Fetch paginated receipt line items collection

`receivedDirectMessage`

Fetch received direct message via ID

`receivedDirectMessages`

Fetch paginated Received Direct Messages collection

`receivedFax`

Fetch Received Fax by ID

`receivedFaxes`

Fetch paginated Received Faxes collection

`recentFoods`

Fetch recent food items

`recurringAppointment`

Query a single recurring appointment

`recurringForms`

Fetch paginated recurring forms collection

`recurringPayment`

Fetch a recurring payment by id

`recurringPayments`

Fetch paginated recurring payments collection

`referral`

Fetch Referral by ID

`referringPhysician`

Get referring physician based on id

`referringPhysicians`

all referring physicians based on current user

`requestedFormCompletion`

fetch a requested form completion by id

`requestedFormCompletions`

Fetch paginated requested form completions collection

`requestedPayment`

fetch a requested payment (invoice) by id

`requestedPayments`

Fetch paginated Requested Payments collection

`savedFilter`

Fetch specific saved filter

`savedFilters`

Fetch paginated saved filters collection

`scheduledMessageBlasts`

Fetch paginated scheduled message blasts collection

`scheduledUserPackageSelections`

Fetch paginated scheduled user package selections collection

`sdkConfig`

SDK configuration

`sentDirectMessage`

Fetch sent direct message via ID

`sentDirectMessages`

Fetch paginated Sent Direct Messages collection

`sentFax`

Fetch sent Fax by ID

`sentFaxes`

Fetch paginated Sent Faxes collection

`sentNotificationRecord`

Fetch a single notification record by ID.

`sentNotificationRecords`

Fetch paginated sent notification records collection

`sentWebhooks`

Fetch paginated SentWebhooks collection. SentWebhook records are available for 180 days.

`servingSizes`

Fetch paginated serving sizes collection

`shareNotePreview`

A HTML string of charting note answers

`shareable`

A document or folder that can be shared with users or groups

`showScheduledTab`

Should current user see scheduled chat tab

`signedStreamName`

Get the signed stream name for a given stream name

`smartPhrases`

Fetch user smart phrases

`startingSuperBillCptCodes`

initial cpt codes for a new super bill

`startingSuperBillIcd10s`

initial icd10 codes for a new super bill

`stateLicenses`

Fetch paginated state licenses collection

`stripeBankAccount`

Default Stripe bank account object associated to a practitioner stripe account

`stripeCompany`

Information about the user's stripe company

`stripeCountries`

An array containing information about countries that stripe supports

`stripeCountry`

An object containing info about a country that stripe supports

`stripeCustomerDetails`

Fetch paginated stripe customer details collection

`subGoals`

Fetch paginated subgoals collection

`subscription`

Get the current users subscription

`superBill`

fetch a superbill by id

`superBills`

Fetch paginated super bills collection

`surescriptsReportedMedicationHistory`

Fetch medication history from the Surescripts history (via Dosespot). Patient consent must be confirmed via the API before calling.

`tags`

A collection of tags related to current patient/provider/organization

`tagsPaginated`

A paginated collection of tags related to current patient/provider/organization

`task`

`tasks`

All tasks assigned to a provider or client

`timesForRange` deprecated

`transactions`

fetch transactions for the current user

`transfers`

fetch transfers for the current user

`treatmentPlans`

Fetch an array of treatment plans and recommended products from Fullscript given a user id

`unassociatedCompletedOnboardingItems`

Fetch paginated unassociated completed onboarding items collection

`ungroupedCourseMemberships`

Fetch paginated ungrouped course memberships collection

`user`

Fetch a user by ID

`userGroup`

fetch a user group by id

`userGroups`

Fetch paginated user groups collection

`userPackageSelections`

Fetch collection of all purchased packages

`users`

Fetch paginated patients collection (use organizationMembers query for providers)

`validateCoupon`

Check if a coupon is valid, and return the new price (considered public)

`validateResetPasswordToken`

Check if a reset password token is valid

`validateSignupToken`

Check if a signup token is valid

`visualizeDashboard`

Fetch static Visualize dashboard by type

`waterIntakeEntry`

`webhooks`

Fetch paginated Webhooks collection

`whitelabelSetting`

Whitelabel setting to use

`writeOff`

Fetch Write Off by ID

`zoomSdkJwt`

Generate a JWT to be used in the client-side Zoom SDK. This is just available on production, and requires your account to be approved by Healthie. The JWT is valid for 1 day.

## Mutations

`addPharmacy`

Add a pharmacy to the user

`asyncBulkCreateOrganizationMemberships`

async bulk create OrganizationMemberships for an organization

`bulkApply`

Apply selected tags on a specific user

`bulkApplyCarePlanTemplate`

Apply care plan to the passed array of clients and/or groups

`bulkCreateAvailability`

bulk create Availability

`bulkCreateEntries`

creates bulk Entries (intended for apple health only for the time being)

`bulkCreateOrganizationMemberships`

bulk create OrganizationMemberships for a user

`bulkDeleteAvailability`

Bulk delete Availability records by IDs. Use with caution. This mutation does not trigger webhooks and bulk deleted availability is not recoverable. .

`bulkDeleteTasks`

Delete tasks

`bulkUpdateCardIssues`

Update unseen card issues on a provider

`bulkUpdateCarePlanUsers`

Trigger notification email or care plan activation for each user related to the selected care plans. In case of activation, a group care plan will be activated for each user of user\_group(unless a user already have an active care plan). If you want to activate selected care plan for only one user(user of group) use ToggleCarePlanStatusForSpecificUser mutation

`bulkUpdateClients`

Update multiple clients at once. Will change user group for multiple clients if user\_group\_id passed, otherwise clients will be archived

`cancelMobileHealthDataSnapshot`

Cancels a mobile health data snapshot that encountered an error during upload or was abandoned by the mobile app

`cancelRecurringPayment`

Cancels the recurring payment for a patient.

`changeDevicesAvailability`

disabled devices in video chat

`clearUnreconciledObjects`

Delete unreconciled allergies/problems/medications

`completeCcdaReconciliation`

Complete a CCDA Reconciliation, based on user choice

`completeCheckout`

Complete the checkout for booking or buying

`completeCourseDocument`

Create CompletedCourseItem for related document

`convertGeneratedFormAnswerGroup`

Converts a generated form answer group to a form answer group

`copyCourse`

Copy a Course

`copyCustomModule`

Copy Custom Module

`copyCustomModuleForm`

copy Custom Module Form

`copyOffering`

Copy an Offering

`createAcceptedInsurancePlan`

Create Accepted Insurance Plans

`createAddendum`

Create a new addendum for the selected charting note

`createAllergySensitivity`

Create AllergySensitivity

`createAnnouncement`

Create Announcement

`createApiKey`

create API Key. This capability needs to be turned on for your account first

`createAppleHealth`

Create AppleHealth

`createAppointment`

create appointment mutation for providers. Clients use the completeCheckout mutation

`createAppointmentFormAnswerGroupConnection`

Create a connection between a form answer group and an appointment.

`createAppointmentRequest`

Create a new appointment request as a part of the booking flow

`createAppointmentSetting`

create an Appointment Setting

`createAppointmentType`

create Appointment Type

`createAppointmentTypeCptCode`

Create an Appointment Type CPT Code Object

`createAutoTaskGenerator`

Create auto task generator

`createAutomatedInsuranceBillingSetting`

create automated insurance billing setting

`createAvailability`

Create availability

`createAvailabilityWithAppointmentTypes`

Create a one-time availability associated with multiple appointment types

`createBillingItem`

create billing item

`createBrand`

create Brand

`createCarePlan`

Create and return a care plan

`createCarePlanRecommendationCategory`

`createChangeHealthPatient`

creates ChangeHealth patient record

`createChatSetting`

create an Chat Setting

`createClient`

Create a Client

`createClientRestrictionAuthorization`

Create client restriction authorization

`createClientViaForm` deprecated

create a client account via a form (e.g a lead capture form) or match to an existing client by name and email. This endpoint is meant to be called unauthenticated. If you want the client to buy or book something at the same time, use the CompleteCheckout mutation.

`createCms1500`

create CMS1500

`createCognitiveStatus`

Create a CognitiveStatus Object

`createComment`

create Comment

`createCompletedCourseItem`

create CompletedCourseItem

`createCompletedOnboardingItem`

create CompletedOnboardingItem

`createContact`

Creates a Contact

`createConversation`

Create a conversation. Maximum of 256 members allowed per conversation.

`createCourse`

create Course

`createCourseBenefit`

create CourseBenefit

`createCourseItem`

create CourseItem

`createCustomEmail`

create custom email

`createCustomFood`

Create a Custom Food

`createCustomModule`

create Custom Module

`createCustomModuleFileAttachment`

Attach an already uploaded file to a form answer

`createCustomModuleFileAttachmentUploadUrl`

Create a pre-signed expiring upload URL for uploading a custom module file attachment.

`createCustomModuleForm`

create Custom Module Form

`createDocument`

create Document

`createDosespotClinician`

Create dosespot clinician

`createDraft`

create Draft

`createDsiComment`

Create a DSI comment

`createEbook`

create ebook

`createEntry`

creates a new Entry

`createEpisodeOfCare`

Create an Episode of Care

`createExternalCalendar`

Create an External Calendar

`createFamilyHistory`

Create Family History

`createFaxAcctInfo`

create Fax Acct Info

`createFaxLineRequest`

Create and return a fax line request

`createFeatureToggle`

Create a FeatureToggle and Return FeatureToggle

`createFitbit`

Create Fitbit

`createFolder`

create Folder

`createFormAnswerFileAttachment`

Attach an already uploaded file to a form answer

`createFormAnswerFileAttachmentUploadUrl`

Create a pre-signed expiring upload URL for uploading a form answer file attachment.

`createFormAnswerGroup`

create FormAnswerGroup

`createFormAnswerGroupSigning` deprecated

Create FormAnswerGroupSigning

`createFullscriptPractitioner`

Create a Fullscript practitioner account using the Fullscript API

`createFunctionalStatus`

Create a FunctionalStatus Object

`createGoal`

create Goal

`createGoalHistory`

create Goal History

`createGoogleFit`

Create GoogleFit

`createGroup`

Create a Group

`createHealthConcern`

Create a HealthConcern Object

`createImmunization`

Create an Immunization

`createImplantableDeviceUser`

Create Implantable Device User association

`createImportDataRequest`

Create an import data request

`createInsuranceAuthorization`

create an insurance authorization

`createInsurancePayment`

Create a manual insurance payment

`createInsurancePlan`

Create Insurance Plan

`createInternalComment`

Create an internal comment on a task or other commentable object.

`createLabOrder`

Create Lab Order

`createLocation`

create Location

`createMeal`

Create a Meal

`createMedication`

Create Medication

`createMessageBlast`

create Message Blast

`createMobileHealthDataIntegration`

Create Mobile Health Data Integration

`createMobileHealthDataSnapshot`

Creates mobile health data snapshot record

`createNote`

Create a note. Cannot create notes in conversations exceeding 256 members.

`createNotificationContact`

create a Notification Contact

`createOffering`

create offering

`createOfferingCoupon`

Create an Offering Coupon

`createOfficeallySftpAccount`

create OfficeallySftpAccount

`createOnboardingFlow`

create OnboardingFlow

`createOnboardingItem`

create OnboardingItem

`createOrAddToWaterIntakeEntry`

creates a new entry or add to existing water intake entry for the day

`createOrganization`

create Organization

`createOrganizationCptCode`

Create an Organization CPT Code Object

`createOrganizationMembership`

create OrganizationMembership

`createPartner`

Creates a Partner

`createPaymentIntent`

Create a Stripe Payment Intent. Currently used for supporting additional payment methods via a custom front-end. When the payment succeeds, Healthie will receive a webhook and automatically complete the checkout.

`createPdfLetterheadTemplate`

Create \`PdfLetterheadTemplate\`

`createPermissionTemplate`

create Permission Template

`createPersonalizationQuestionnaire`

create Personalization Questionnaire

`createPreferredMedicalCode`

Create favorite CPT/ICD code

`createProcedure`

Create a Procedure Object

`createProduct`

Create a product

`createProviderAcceptedInsurancePlans`

Create one or more accepted insurance plan associations for a specific provider.

`createProviderCptCodes`

Create ProviderCPTCode Objects

`createRecommendation`

Create a care plan recommendation

`createReferral`

Create new Referring Physician

`createReferringPhysician`

Create new Referring Physician

`createRequestedFormCompletion`

create requested form, creates the RequestedFormCompletion in the background and returns only a status message unless using the legacy recipient\_id argument which returns the created RequestedFormCompletion

`createRequestedPayment`

create requested payment

`createRupaOrder`

Create a Rupa order

`createSavedFilter`

Create a new saved filter

`createSecondaryClaim`

Create a secondary claim from a primary claim for COB submission

`createSentDirectMessage`

Create a sent direct message

`createSentFax`

create Sent Fax

`createSetupIntent`

Create a Stripe Setup Intent. Used for setting up payment methods for future usage without immediately charging.

`createSharings`

Create document or folder sharings for clients, providers, and/or groups

`createSmartPhrase`

Create a Smart Phrase

`createSmokingStatus`

Create a Smoking Status

`createStripeCustomerDetail`

Creates a new payment card

`createSubscription`

create Subscription

`createSuperBill`

create super bill

`createTag`

Create a custom user tag

`createTask`

Create a task for provider

`createUniqueDeviceIdentifier`

Create a UniqueDeviceIdentifier Object

`createVisitor`

Creates a Visitor

`createWebhook`

Create Webhook

`createWriteOff`

Create a Write-off

`deleteAcceptedInsurancePlan`

Destroy Accepted Insurance Plan

`deleteAllergySensitivity`

Destroy AllergySensitivity

`deleteAnnouncement`

Destroy Announcement

`deleteApiKey`

Destroy API Key

`deleteAppleHealth`

Destroy AppleHealth

`deleteAppointment`

Delete an Appointment

`deleteAppointmentFormAnswerGroupConnection`

Remove a form\_answer\_groups connection to an appointment

`deleteAppointmentRequest`

Delete an existing appointment request

`deleteAppointmentType`

Destroy an AppointmentType

`deleteAppointmentTypeCptCode`

Delete a AppointmentTypeCptCode Object

`deleteAutoTaskGenerator`

Delete auto task generator

`deleteAvailability`

delete Availability

`deleteBillingItem`

Destroy a Billing Item

`deleteCarePlan`

Destroy a Care Plan

`deleteCarePlanConnection`

Remove connection for related item(document/goal/recommendation)

`deleteCarePlanRecommendationCategory`

`deleteClientRestrictionAuthorization`

Delete client restriction authorization

`deleteCms1500`

Destroy a Cms1500

`deleteCognitiveStatus`

Delete a CognitivesStatus Object

`deleteComment`

Destroy a Comment

`deleteConversationMembership`

Destroy a Conversation Membership

`deleteCourse`

Destroy a Course

`deleteCourseBenefit`

Destroy a Course Benefit

`deleteCourseGroup`

Destroy a Course Group

`deleteCourseItem`

Destroy a Course Item

`deleteCourseMembership`

Destroy a Course Membership

`deleteCustomEmail`

Destroy a Custom Email

`deleteCustomFood`

Destroy a Custom Food

`deleteCustomModule`

Destroy an CustomModule

`deleteCustomModuleFileAttachment`

Delete a CustomModule file attachment. If the underlying blob is shared by other attachments, only the attachment record is removed. Otherwise, the blob is purged from storage. Requires edit permissions on the CustomModule.

`deleteCustomModuleForm`

Destroy an CustomModuleForm

`deleteDexcomConnection`

Destroy Dexcom Connection

`deleteDocument`

Destroy a Document

`deleteEntry`

Destroy a Entry

`deleteEpisodeOfCare`

Delete an Episode of Care

`deleteExternalCalendar`

Destroy an External Calendar

`deleteFamilyHistory`

Delete a Family History Condition

`deleteFaxAcctInfo`

destroy Fax Acct Info

`deleteFitbit`

Destroy Fitbit

`deleteFolder`

Destroy a Folder

`deleteFormAnswerFileAttachment`

Delete a FormAnswer file attachment

`deleteFormAnswerGroup`

Destroy a Form Answer Group

`deleteFormAnswerGroupSigning`

Destroy FormAnswerGroupSigning

`deleteFunctionalStatus`

Delete a FunctionalStatus Object

`deleteGoal`

Destroy a Goal

`deleteGoalHistory`

Destroy a Goal GoalHistory

`deleteGoogleFit`

Destroy GoogleFit

`deleteHealthConcern`

Delete a HealthConcern Object

`deleteImplantableDeviceUser`

Delete an Implantable Device User association

`deleteInsuranceAuthorization`

delete an insurance authorization

`deleteInsurancePlan`

Delete Insurance Plan

`deleteLocation`

Destroy a Location

`deleteManualInsurancePayment`

Delete a manual insurance payment (soft delete)

`deleteMeal`

Destroy a Meal

`deleteMedication`

Destroy Medication

`deleteMobileHealthDataIntegration`

Destroy Mobile Health Data Integration

`deleteNote`

Destroy a Note

`deleteNotificationContact`

delete a Notification Contact

`deleteOffering`

Destroy an Offering

`deleteOfferingCoupon`

Destroy an Offering Coupon

`deleteOnboardingFlow`

Destroy a OnboardingFlow

`deleteOnboardingItem`

Destroy a OnboardingItem

`deleteOrganizationCptCode`

Delete a OrganizationCptCode Object

`deleteOrganizationInfo`

Destroy an organization info

`deleteOrganizationMembership` deprecated

Destroy a Organization Membership

`deletePermissionTemplate`

delete Permission Template

`deletePreferredMedicalCode`

Delete favorite CPT/ICD code

`deleteProcedure`

Delete a Procedure Object

`deleteProduct`

Delete a product

`deleteProviderAcceptedInsurancePlan`

Delete an existing provider accepted insurance plan

`deleteProviderCptCode`

Delete a ProviderCptCode Object

`deleteReceivedFax`

Destroy a received fax

`deleteRecommendation`

Destroy a care plan recommendation

`deleteRecurringForm`

Delete recurring form request

`deleteReferral`

Delete referral

`deleteReferringPhysician`

Delete referring physician

`deleteRequestedFormCompletion`

Destroy a requested form

`deleteRequestedPayment`

destroy requested payment

`deleteSavedFilter`

Delete a saved filter

`deleteShapaConnection`

Destroy Shapa Connection

`deleteSharings`

Destroy document or folder sharings for clients, providers, and/or groups

`deleteSmartPhrase`

Destroy a Smart Phrase

`deleteSmokingStatus`

Delete a Smoking Status

`deleteStripeCustomerDetail`

Deletes a payment card

`deleteSuperBill`

Destroy a Super Bill

`deleteTag`

Delete a custom user tag

`deleteTask`

Destroy a task

`deleteTranscript`

Delete a transcript (realtime capture or processed recording)

`deleteUniqueDeviceIdentifier`

Delete a UniqueDeviceIdentifier Object

`deleteUserGroup`

Delete a Group

`deleteWebhook`

Destroy Webhook

`deleteWithingsConnection`

Destroy Withings Connection

`deleteWriteOff`

Delete a write-off

`deleteZoomRecordingFile`

Delete a Zoom Recording File either via ID OR appointment and file ID

`destroyInternalComment`

Destroy an internal comment on a task or other commentable object.

`destroyPdfLetterheadTemplate`

Delete \`PdfLetterheadTemplate\`

`dismissAllAnnouncements`

Dismiss All Announcements For A User

`dismissAnnouncement`

Dismiss Announcement

`editAvailability`

edit Availability

`editAvailabilityWithAppointmentTypes`

Edit a one-time availability associated with multiple appointment types

`expireWebhookSignature`

Expires the webhook signature

`exportCarePlanToTemplate`

Creates a template from existing Care Plan. Original object is not touched

`exportClientEhi`

Export Client EHI data

`generateChartingPdf`

Generate a PDF of charting notes for a client

`healthAssessmentServiceSignup` deprecated

Sign up Healthie User in the Health Assessment Service

`ingestMedicationsFromSurescripts`

ingest med history from surescripts

`linkEncounterToEpisodeOfCare`

Link patient encounter(s) to an Episode of Care

`lockFormAnswerGroup`

Lock \`FormAnswerGroup\`

`logMedicationHistoryConsent`

Log that a patient has consented to having their medication history pulled via Surescripts/Dosespot

`mergeClients`

all data related to the merging account (form answers, billing items, charting notes, etc) will be associated with the selected account after merging. The selected account's client profile information will remain unchanged (name, DOB, etc)

`parseCcdaDocument`

Import client from a CCDA file

`pauseCourseGroup`

Pause a course group, bulk-pausing all active member enrollments

`pauseCourseMembership`

Pause a client's program enrollment

`processMobileHealthDataSnapshot`

Mobile app usage only. Downloads and processes mobile health categories like: 'Heart Rate', 'Steps', etc.

`refetchChangeHealthLabOrder`

refetch ChangeHealth Lab Orders for a specified patient

`rejectGeneratedFormAnswerGroup`

Rejects an AI-generated form answer group

`removeAppliedTag`

Remove applied tag on a specific user

`removeDraft`

remove Draft

`removeUserFromGroupCarePlan`

Remove group care plan user connection for a specific user

`requestIntegration`

Send an email asking support to enable a given integration.

`resendSentFax`

resend Sent Fax

`resetDefaultPdfLetterheadTemplate`

Set system default \`PdfLetterheadTemplate\` for current\_user's organization

`resetMfa`

Unenrolls the user from multi-factor authentication (MFA), removing their current MFA devices and requiring them to re-enroll if MFA is enforced. Requires permission to edit the target user.

`resetPassword`

send the human a password reset email

`resumeCourseGroup`

Resume a paused course group, bulk-resuming all paused member enrollments

`resumeCourseMembership`

Resume a paused program enrollment

`resyncRupaLabOrders`

Resync existed rupa lab orders data for a specific rupa connection of the current user

`revokeToken`

revoke token or API key.

`runEligibilityCheck`

Run an eligibility check on a policy

`sendCarePlanEmail`

Trigger care plan email for given client

`sendSpeakToTrainerNotification` deprecated

Send the trainer an email that the client wants to speak to them

`sendTestWebhook`

Sends a test webhook to the specified URL

`setCustomModuleFormScribeInstructions`

Set or clear form-level AI Scribe instructions on a charting CustomModuleForm.

`setDefaultPdfLetterheadTemplate`

Set \`PdfLetterheadTemplate\` default for the org

`shareAnswersAsDocument`

Add form answer group answers as document viewable by client

`shareCourse`

share Course with another provider

`shareCustomModuleForm`

share Custom Module Form

`signFormAnswerGroup`

Sign \`FormAnswerGroup\`

`signIn`

SignIn

`signUp`

Sign up

`submitSecondaryClaim`

Submit secondary claims with COB data to ClaimMD

`toggleCarePlanStatusForSpecificUser`

Deactivate/activate a group/single Care Plan for a given user

`unlinkEncounterToEpisodeOfCare`

Unlink patient encounter(s) from an Episode of Care

`unlockFormAnswerGroup`

Unlock \`FormAnswerGroup\`

`unsubscribeFromNotification`

Update a Notification Setting to unsubscribe from a specific notification type

`updateAddendum` deprecated

THIS MUTATION DOES NOTHING, AND SHOULD NOT BE USED.

`updateAllergySensitivity`

Update AllergySensitivity

`updateAnnouncement`

Update Announcement

`updateAppleHealth`

Update AppleHealth

`updateAppointment`

Update the Appointment

`updateAppointmentInclusion`

Update AppointmentInclusion

`updateAppointmentRequest`

Update an existing appointment request

`updateAppointmentSetting`

update Appointment Setting

`updateAppointmentType`

Update an Appointment Type and return Appointment Type

`updateAppointmentTypeCptCode`

Update a AppointmentTypeCptCode Object

`updateAutoTaskGenerator`

Update auto task generator

`updateAutomatedInsuranceBillingSetting`

update automated insurance billing setting

`updateBillingItem`

Update a BillingItem

`updateBrand`

Update a Brand and return Brand

`updateByTemplate`

Update Care Plan by Care Plan Template

`updateCalendarViewSetting`

Update and return calendar view setting

`updateCalorieLevel` deprecated

Update Calorie Levels in the Health Assessment Service

`updateCarePlan`

Update and return a Care Plan

`updateCarePlanRecommendationCategory`

`updateChangeHealthAccount`

Update ChangeHealthAccount (used for Labs)

`updateChargeBack`

Update ChargeBack

`updateChatSetting`

update Chat Setting

`updateClient`

Update Client

`updateCms1500`

update CMS1500

`updateCognitiveStatus`

Update a CognitiveStatus Object

`updateConversation`

Update a conversation and return the conversation. Maximum of 256 members allowed per conversation.

`updateConversationMembership`

Update a ConversationMembership and return ConversationMembership

`updateCourse`

Update a Course

`updateCourseGroup`

update a Course Group

`updateCourseItem`

Update a CourseItem

`updateCourseMembership`

update a Course Membership

`updateCustomEmail`

Update a Custom Email

`updateCustomFood`

Update a Custom Food

`updateCustomModule`

Update an Custom Module and return Custom Module

`updateCustomModuleForm`

Update an Custom Module Form and return Custom Module Form

`updateDocument`

Update a Document and return Document

`updateDsiComment`

Update a DSI comment

`updateEntry`

Updates an Entry and returns an Entry

`updateEpisodeOfCare`

Update an Episode of Care

`updateExternalCalendar`

Update an External Calendar

`updateFamilyHistory`

Update Family History

`updateFaxAcctInfo`

update Fax Acct Info

`updateFeatureToggle`

Update a FeatureToggle and Return FeatureToggle

`updateFitbit`

Update Fitbit

`updateFolder`

Update a Folder and return Folder

`updateFormAnswerGroup`

update FormAnswerGroup

`updateFunctionalStatus`

Update a FunctionalStatus Object

`updateGeneratedFormAnswerGroupFeedback`

Updates feedback for an AI-generated form answer group

`updateGoal`

Update a Goal

`updateGoogleFit`

Update GoogleFit

`updateGroupCarePlan`

Updates the care plan status for groups

`updateHealthConcern`

Update a HealthConcern Object

`updateHuman`

Update a Human

`updateImmunization`

Update an Immunization and return Immunization

`updateImplantableDeviceUser`

Update Implantable Device User association

`updateInsuranceAuthorization`

update an insurance authorization

`updateInsurancePaymentDepositStatus`

Update the deposit status of an insurance payment

`updateInsurancePlan`

Update Insurance Plan

`updateInternalComment`

Update an internal comment on a task or other commentable object. Only usable by the comment author.

`updateLabOrder`

Update Lab Order

`updateLocation`

update Location

`updateMacronutrientSplit` deprecated

Update Macronutrient Split in the Health Assessment Service

`updateManualInsurancePayment`

Update a manual insurance payment

`updateMeal`

Update a Meal

`updateMedication`

Update Medication

`updateNote`

Update a Note

`updateNoteScheduler`

Update a Note Scheduler and return NoteSchedulerType

`updateNotification`

update a notification

`updateNotificationContact`

Update a Notification Contact

`updateNotificationRecords`

Update multiple notification records at once

`updateNotificationSetting`

Update a Notification Setting and return Notification Setting

`updateNotifications`

update multiple notifications at once

`updateOffering`

Update an Offering

`updateOfficeallySftpAccount`

update OfficeallySftpAccount

`updateOnboardingFlow`

Update a OnboardingFlow and return OnboardingFlow

`updateOnboardingItem`

Update a OnboardingItem and return OnboardingItem

`updateOrganization`

Update Organization

`updateOrganizationCptCode`

Update a OrganizationCptCode Object

`updateOrganizationMember`

Update org members

`updateOrganizationMembership`

Update a OrganizationMembership

`updateOrganizationUiConfiguration`

`updatePdfLetterheadTemplate`

Update \`PdfLetterheadTemplate\`

`updatePermissionTemplate`

update Permission Template

`updatePolicy`

Update a policy

`updateProcedure`

Update a Procedure Object

`updateProduct`

Update a product

`updateProviderCptCodes`

Update ProviderCptCode Objects

`updateReceivedDirectMessage`

Update a Received Direct Message

`updateReceivedFax`

update a received fax

`updateRecommendation`

Update a care plan recommendation

`updateRecurringForm`

update a recurring form

`updateReferral`

Update Referral

`updateReferringPhysician`

Update Referring Physician

`updateRequestedPayment`

update requested payment

`updateSavedFilter`

Update an existing saved filter

`updateSecondaryClaim`

Update COB overrides on a secondary claim

`updateSmartPhrase`

Update a Smart Phrase

`updateSmokingStatus`

Update a Smoking Status

`updateState`

Archive/Unarchive a Course

`updateStripeCustomerDetail`

Updates a payment card

`updateStripeVerificationDetails`

Update Stripe Verification Details

`updateSubscription`

update Subscription

`updateSuperBill`

Update a SuperBill

`updateTag`

Update a custom user tag

`updateTask`

Update a task for provider

`updateTasksBulk`

Bulk update multiple tasks with completion status, seen status, and filtering options. Can update all tasks matching filters or specific tasks by ID.

`updateUniqueDeviceIdentifier`

Update a UniqueDeviceIdentifier Object

`updateUser`

Update the current user, or a patient that the current user has access to. To update other org members, use updateOrganizationMembership

`updateUserAppointmentPricing`

Updates the appointment pricing for this user

`updateUserGroup`

Update a Group

`updateWebhook`

Update Webhook

`updateWriteOff`

Update a Write-off

`uploadBatchToCandidHealth`

Upload a CMS1500 batch to CandidHealth

`uploadBatchToChangeHealth` deprecated

Upload a CMS1500 batch to ChangeHealth

`uploadBatchToOfficeally`

Upload a CMS1500 batch to OfficeAlly

`uploadCms1500sToIntegrations`

Upload a CMS1500 to integrations: ChangeHealth, OfficeAlly, CandidHealth

`validateVerificationToken`

Verify 2FA code for Human

## Objects

`AcceptedInsurancePlan`

`AcceptedInsurancePlanConnection`

`AcceptedInsurancePlanEdge`

`AdvanceAppointmentPrice`

`AdvanceAppointmentPriceEdge`

`AdvanceAppointmentPricePaginationConnection`

`Affiliate`

`AllergySensitivity`

`Announcement`

`AnnouncementEdge`

`AnnouncementPaginationConnection`

`ApiKey`

`ApiKeyEdge`

`ApiKeyPaginationConnection`

`AppleHealth`

`AppliedTag`

`AppliedTagEdge`

`AppliedTagPaginationConnection`

`Appointment`

`AppointmentAutocompleteForm`

`AppointmentBookingWarning`

`AppointmentCreditChange`

`AppointmentCreditChangeEdge`

`AppointmentCreditChangePaginationConnection`

`AppointmentDataType`

`AppointmentEdge`

`AppointmentFrequencyDataType`

`AppointmentInclusionType`

`AppointmentLocation`

`AppointmentLocationEdge`

`AppointmentLocationPaginationConnection`

`AppointmentPaginationConnection`

`AppointmentPerDayData`

`AppointmentPerTypePerDayData`

`AppointmentPerTypePerUserData`

`AppointmentPerUserData`

`AppointmentPricingInfoType`

`AppointmentRequestSlotType`

`AppointmentRequestType`

`AppointmentRequestTypeConnection`

`AppointmentRequestTypeEdge`

`AppointmentSetting`

`AppointmentSummaryData`

`AppointmentType`

`AppointmentTypeAppointmentCountData`

`AppointmentTypeCptCodeType`

`AppointmentTypeCredit`

`AppointmentTypeEdge`

`AppointmentTypeFormConnection`

`AppointmentTypePaginationConnection`

`AppointmentWorkflowStatus`

`AppointmentWorkflowStatusAppointmentType`

`AppointmentWorkflowStatusChartNoteType`

`AppointmentWorkflowStatusClientType`

`AppointmentWorkflowStatusCms1500Type`

`AppointmentWorkflowStatusConnection`

`AppointmentWorkflowStatusEdge`

`AppointmentWorkflowStatusInvoiceType`

`AppointmentWorkflowStatusProviderType`

`AssumedBrand`

`AuditEvent`

`AuditEventEdge`

`AuditEventPaginationConnection`

`AuditEventResourceChange`

`AutoTaskGenerator`

`AutoTaskGeneratorEdge`

`AutoTaskGeneratorPaginationConnection`

`AutomatedInsuranceBillingSetting`

`AutoscoredSectionType`

`Availability`

`Benefit`

`BillingConfiguration`

`BillingItem`

`BillingItemEdge`

`BillingItemPaginationConnection`

`BodyReport`

`Brand`

`BrandInfo`

`BulkDeleteAvailabilityPayload`

`CalendarColorScheme`

`CalendarViewSetting`

`CallReference`

`CancelMobileHealthDataSnapshotPayload`

`CancellationReason`

`CandidHealthConnection`

`CarePlan`

`CarePlanConnection`

`CarePlanEdge`

`CarePlanPaginationConnection`

`CarePlanRecommendationCategory`

`CdaActivityEvent`

`CdaActivityEventEdge`

`CdaActivityEventPaginationConnection`

`ChangeClaimSubmitter`

`ChangeDevicesAvailabilityPayload`

`ChargeBack`

`ChargeBackEdge`

`ChargeBackEvidence`

`ChargeBackPaginationConnection`

`ChargeDisputeType`

`ChargeDisputeTypeConnection`

`ChargeDisputeTypeEdge`

`ChartingItemType`

`ChartingNoteAddendumType`

`ChatSetting`

`Claim`

`ClaimCptCode`

`ClaimDiagnosis`

`ClaimEdge`

`ClaimEligibilityCheck`

`ClaimEligibilityCheckErrors`

`ClaimIcdCode`

`ClaimInsurancePlan`

`ClaimLocation`

`ClaimMdMessage`

`ClaimOtherIdNumber`

`ClaimPaginationConnection`

`ClaimPatient`

`ClaimPlaceOfService`

`ClaimPolicy`

`ClaimPolicyHolder`

`ClaimProvider`

`ClaimReferralInfo`

`ClaimReferringPhysician`

`ClaimServiceLine`

`ClaimSubmission`

`ClaimSubmissionEdge`

`ClaimSubmissionPaginationConnection`

`ClientPortalSetting`

`ClientRestrictionAuthorization`

`ClientSource`

`Cms1500`

`Cms1500Edge`

`Cms1500PaginationConnection`

`Cms1500Policy`

`CobAdjustment`

`CobServiceLineAdjustment`

`CognitiveStatus`

`ColorCode`

`ColorCodeOption`

`Comment`

`CommentEdge`

`CommentPaginationConnection`

`CompleteCcdaReconciliationPayload`

`CompletedCourseItem`

`CompletedOnboardingItem`

`CompletedOnboardingItemEdge`

`CompletedOnboardingItemPaginationConnection`

`ContactType`

`Conversation`

`ConversationEdge`

`ConversationMembership`

`ConversationMembershipEdge`

`ConversationMembershipPaginationConnection`

`ConversationMembershipsAllCounts`

`ConversationPaginationConnection`

`CoordinationOfBenefits`

`Course`

`CourseBenefit`

`CourseCompletionInfoGroupsType`

`CourseCompletionInfoIndividualsType`

`CourseCompletionInfoType`

`CourseEdge`

`CourseGroup`

`CourseItem`

`CourseItemEdge`

`CourseItemPaginationConnection`

`CourseMembership`

`CourseMembershipEdge`

`CourseMembershipPaginationConnection`

`CoursePaginationConnection`

`CptCode`

`CptCodeEdge`

`CptCodePaginationConnection`

`CptCodesCms1500`

`CptCodesPolicy`

`CptCodesSuperBill`

`CreateAvailabilityWithAppointmentTypesPayload`

`CreateChangeHealthPatientPayload`

`CreateClientViaFormPayload`

`CreateCustomModuleFileAttachmentPayload`

`CreateCustomModuleFileAttachmentUploadUrlPayload`

`CreateInternalCommentPayload`

`CreateMobileHealthDataIntegrationPayload`

`CreateMobileHealthDataSnapshotPayload`

`CreateSecondaryClaimPayload`

`CustomEmail`

`CustomEmailEdge`

`CustomEmailPaginationConnection`

`CustomMetric`

`CustomMetricOverride`

`CustomModule`

`CustomModuleConditionType`

`CustomModuleEdge`

`CustomModuleForm`

`CustomModuleFormEdge`

`CustomModuleFormPaginationConnection`

`CustomModulePaginationConnection`

`CustomSidebarOverride`

`DayRangeType`

`DeleteCustomModuleFileAttachmentPayload`

`DeleteMobileHealthDataIntegrationPayload`

`DeleteTranscriptPayload`

`DestroyInternalCommentPayload`

`DexcomConnection`

`Diagnosis`

`DirectMessageAttachment`

`Discount`

`Document`

`DocumentEdge`

`DocumentPaginationConnection`

`DocumentViewing`

`DocumentViewingEdge`

`DocumentViewingPaginationConnection`

`DosageType`

`DoseSpot`

`Draft`

`DrugAllergenType`

`DsiComment`

`ELabsSettings`

`EditAvailabilityWithAppointmentTypesPayload`

`EligibilityCheck`

`EmbedWidgetStepType`

`Entry`

`EntryEdge`

`EntryPaginationConnection`

`EpisodeOfCare`

`EpisodeOfCareConnection`

`EpisodeOfCareEdge`

`Era`

`EraAdjustment`

`EraConnection`

`EraEdge`

`EraServiceLine`

`EraServiceLineConnection`

`EraServiceLineEdge`

`ExternalCalendar`

`ExternalCalendarConnection`

`ExternalCalendarEdge`

`FamilyHistoryCondition`

`FaxLineRequest`

`FeatureToggle`

`FieldError`

`FileAttachment`

`Fitbit`

`Folder`

`FolderEdge`

`FolderPaginationConnection`

`Food`

`FoodEdge`

`FoodItem`

`FoodNutrient`

`FoodPaginationConnection`

`FormAnswer`

`FormAnswerGroup`

`FormAnswerGroupAuditEvent`

`FormAnswerGroupEdge`

`FormAnswerGroupPaginationConnection`

`FormAnswerGroupSigning`

`FormAnswerGroupUserConnection`

`FormHistory`

`FormHistoryEdge`

`FormHistoryPaginationConnection`

`FormTypesToRequest`

`FullscriptPractitionerType`

`FullscriptPractitionerTypeType`

`FullscriptProductType`

`FullscriptTreatmentPlanType`

`FunctionalStatus`

`GeneratedFormAnswerGroupType`

`GeneratedFormAnswerType`

`GeneratedSummary`

`Goal`

`GoalDataType`

`GoalEdge`

`GoalHistory`

`GoalHistoryEdge`

`GoalHistoryPaginationConnection`

`GoalInstance`

`GoalInstanceEdge`

`GoalInstancePaginationConnection`

`GoalOverallCompletionRateInfo`

`GoalPaginationConnection`

`GoalStreakInfo`

`GoalTemplate`

`GoalTemplateEdge`

`GoalTemplatePaginationConnection`

`GoogleFit`

`GroupCarePlanUserConnection`

`HealthAssessment`

`HealthAssessmentRecommendation`

`HealthAssessmentServiceSignupPayload`

`HealthConcern`

`HealthReport`

`HttpHeader`

`Human`

`IcdCode`

`IcdCodeEdge`

`IcdCodePaginationConnection`

`IcdCodesCms1500`

`IcdCodesIndividualClientNote`

`IcdCodesPolicy`

`IcdCodesSuperBill`

`Immunization`

`ImplantableDevice`

`ImplantableDeviceUser`

`ImportDataRequest`

`IndividualClientType`

`InsuranceAuthorizationChartType`

`InsuranceAuthorizationType`

`InsurancePayment`

`InsurancePaymentConnection`

`InsurancePaymentEdge`

`InsurancePlan`

`InsurancePlanEdge`

`InsurancePlanPaginationConnection`

`IntakeFlowItem`

`IntakeFlowItemRequestInfo`

`IntakeFlowType`

`IntegrationButtonConfig`

`IntegrationCategoryType`

`IntegrationCategoryTypeEdge`

`IntegrationCategoryTypePaginationConnection`

`IntegrationDetailsType`

`IntegrationOptionType`

`InternalComment`

`InternalCommentEdge`

`InternalCommentPaginationConnection`

`LabFiltersDataType`

`LabObservationRequest`

`LabObservationResult`

`LabOption`

`LabOptionEdge`

`LabOptionMarker`

`LabOptionPaginationConnection`

`LabOrder`

`LabOrderEdge`

`LabOrderPaginationConnection`

`LabResult`

`LinkUnlinkEncounterToEpisodeOfCare`

`Location`

`LocationEdge`

`LocationPaginationConnection`

`LocationResourceType`

`LockPayload`

`Meal`

`MealEdge`

`MealPaginationConnection`

`MealPlan`

`MedicationHistoryType`

`MedicationHistoryTypeEdge`

`MedicationHistoryTypePaginationConnection`

`MedicationOptionType`

`MedicationType`

`MedicationTypeEdge`

`MedicationTypePaginationConnection`

`MetricDataPointType`

`MetricGraphDataType`

`MobileHealthDataIntegration`

`MobileHealthDataSnapshot`

`MonthlyBillingItemsDataType`

`MultiLineMetricGraphDataType`

`NarxCheck`

`Note`

`NoteEdge`

`NotePaginationConnection`

`NoteScheduler`

`NoteSchedulerEdge`

`NoteSchedulerPaginationConnection`

`Notification`

`NotificationContact`

`NotificationEdge`

`NotificationPaginationConnection`

`NotificationSetting`

`Offering`

`OfferingCoupon`

`OfferingCouponEdge`

`OfferingCouponPaginationConnection`

`OfferingCourse`

`OfferingEdge`

`OfferingGroupVisibility`

`OfferingGroupVisibilityEdge`

`OfferingGroupVisibilityPaginationConnection`

`OfferingImage`

`OfferingImageEdge`

`OfferingImagePaginationConnection`

`OfferingInclude`

`OfferingLabOption`

`OfferingPaginationConnection`

`OfferingProduct`

`OfferingsDataType`

`OfficeallySftpAccount`

`OnboardingFlow`

`OnboardingFlowEdge`

`OnboardingFlowPaginationConnection`

`OnboardingItem`

`Organization`

`OrganizationCptCodeInsuranceFeeType`

`OrganizationCptCodeType`

`OrganizationFeeScheduleCptCodeType`

`OrganizationFeeScheduleCptCodeTypeConnection`

`OrganizationFeeScheduleCptCodeTypeEdge`

`OrganizationInfo`

`OrganizationInfoEdge`

`OrganizationInfoPaginationConnection`

`OrganizationMembership`

`OrganizationMembershipEdge`

`OrganizationMembershipPaginationConnection`

`OtherIdNumber`

`OtherIdNumberEdge`

`OtherIdNumberPaginationConnection`

`PageInfo`

`PatientEncounter`

`PauseCourseGroupPayload`

`PauseCourseMembershipPayload`

`PayoutAccount`

`PayoutAccountEdge`

`PayoutAccountPaginationConnection`

`PdfLetterheadTemplate`

`PermissionTemplateType`

`PermissionTemplateTypeEdge`

`PermissionTemplateTypePaginationConnection`

`Pharmacy`

`PharmacyEdge`

`PharmacyPaginationConnection`

`PlaceOfService`

`PlaceOfServiceEdge`

`PlaceOfServicePaginationConnection`

`Plan`

`Policy`

`PotentialAppointmentSlot`

`PreferredMedicalCode`

`PreferredMedicalCodeEdge`

`PreferredMedicalCodePaginationConnection`

`Prescription`

`PrescriptionDiagnosis`

`PrescriptionMedicationConnection`

`PrescriptionMedicationEdge`

`PriceAndCptPriceType`

`Problem`

`Procedure`

`ProcessMobileHealthDataSnapshotPayload`

`Product`

`ProductEdge`

`ProductPaginationConnection`

`Profession`

`ProviderAcceptedInsurancePlanType`

`ProviderAcceptedInsurancePlanTypeEdge`

`ProviderAcceptedInsurancePlanTypePaginationConnection`

`ProviderAppointmentLocation`

`ProviderApptTypeConnection`

`ProviderBio`

`ProviderCptCodeType`

`ProviderCptCodeTypeEdge`

`ProviderCptCodeTypePaginationConnection`

`ReceiptLineItem`

`ReceiptLineItemEdge`

`ReceiptLineItemPaginationConnection`

`ReceivedDirectMessage`

`ReceivedDirectMessageEdge`

`ReceivedDirectMessagePaginationConnection`

`ReceivedFax`

`ReceivedFaxEdge`

`ReceivedFaxPaginationConnection`

`Recommendation`

`RecurringAppointment`

`RecurringDaysData`

`RecurringForm`

`RecurringFormEdge`

`RecurringFormPaginationConnection`

`RecurringPayment`

`RecurringPaymentEdge`

`RecurringPaymentPaginationConnection`

`Referral`

`ReferralInfo`

`ReferringPhysician`

`ReferringPhysicianEdge`

`ReferringPhysicianPaginationConnection`

`RefetchChangeHealthLabOrderPayload`

`RefundItem`

`RelatedObject`

`Reminder`

`ReportsDateFilterSelection`

`RequestIntegrationPayload`

`RequestedFormCompletion`

`RequestedFormCompletionEdge`

`RequestedFormCompletionPaginationConnection`

`RequestedFormStatusType`

`RequestedPayer`

`RequestedPayment`

`RequestedPaymentEdge`

`RequestedPaymentPaginationConnection`

`RequestedPaymentTemplate`

`RequestedPaymentTemplateEdge`

`RequestedPaymentTemplatePaginationConnection`

`ResetMfaPayload`

`ResumeCourseGroupPayload`

`ResumeCourseMembershipPayload`

`Room`

`SDKConfig`

`SavedFilter`

`SavedFilterEdge`

`SavedFilterPaginationConnection`

`ScheduledUserPackageSelection`

`ScheduledUserPackageSelectionEdge`

`ScheduledUserPackageSelectionPaginationConnection`

`SendSpeakToTrainerNotificationPayload`

`SentDirectMessage`

`SentDirectMessageEdge`

`SentDirectMessagePaginationConnection`

`SentFax`

`SentFaxEdge`

`SentFaxPaginationConnection`

`SentNotificationRecord`

`SentNotificationRecordEdge`

`SentNotificationRecordPaginationConnection`

`SentWebhook`

`SentWebhookEdge`

`SentWebhookPaginationConnection`

`ServingSize`

`ServingSizeEdge`

`ServingSizePaginationConnection`

`SetCustomModuleFormScribeInstructionsPayload`

`ShapaConnection`

`SignPayload`

`SmartPhrase`

`SmartPhraseEdge`

`SmartPhrasePaginationConnection`

`SmokingStatus`

`SmsTemplateWarning`

`SnomedTerm`

`Specialty`

`SsoConnection`

`StateLicense`

`StateLicenseEdge`

`StateLicensePaginationConnection`

`StripeBankAccountType`

`StripeCompanyAddressType`

`StripeCompanyType`

`StripeCountry`

`StripeCustomerDetail`

`StripeCustomerDetailEdge`

`StripeCustomerDetailPaginationConnection`

`StripeInvoice`

`StripePlan`

`SubmitSecondaryClaimPayload`

`Subscription`

`SubscriptionInstance`

`SuperBill`

`SuperBillEdge`

`SuperBillPaginationConnection`

`SymptomOption`

`Tag`

`TagEdge`

`TagPaginationConnection`

`Task`

`TaskEdge`

`TaskPaginationConnection`

`TransactionType`

`Transcript`

`TransferType`

`UniqueDeviceIdentifier`

`UnlockPayload`

`UpdateCalorieLevelPayload`

`UpdateInternalCommentPayload`

`UpdateMacronutrientSplitPayload`

`UpdateSecondaryClaimPayload`

`UpdateUiConfigurationPayload`

`User`

`UserConnection`

`UserEdge`

`UserGroup`

`UserGroupEdge`

`UserGroupPaginationConnection`

`UserNotificationsCount`

`UserPackageSelection`

`UserPackageSelectionEdge`

`UserPackageSelectionPaginationConnection`

`ValidateOfferingCoupon`

`VideoChat`

`VideoChatsSubscriptionPayload`

`VideoUrlDefault`

`VideoUrlOption`

`Visitor`

`VisualizeDashboardType`

`Webhook`

`WebhookEdge`

`WebhookEvent`

`WebhookPaginationConnection`

`WhitelabelSetting`

`WithingsConnection`

`WriteOff`

`ZoomAppointment`

`ZoomCloudRecordingFile`

`ZoomCoHostLink`

`addPharmacyPayload`

`asyncBulkCreateOrganizationMembershipsPayload`

`bulkApplyCarePlanTemplatePayload`

`bulkApplyPayload`

`bulkCreateAvailabilityPayload`

`bulkCreateEntriesPayload`

`bulkCreateOrganizationMembershipsPayload`

`bulkDeleteTasksPayload`

`bulkUpdateCardIssuesPayload`

`bulkUpdateCarePlanUsersPayload`

`bulkUpdateClientsPayload`

`bulkUpdateNotificationRecordsPayload`

`bulkUpdateNotificationsPayload`

`bulkUpdateTasksPayload`

`cancelRecurringPaymentPayload`

`clearUnreconciledObjectsPayload`

`completeCheckoutPayload`

`completeCourseDocumentPayload`

`convertGeneratedFormAnswerGroupPayload`

`copyCoursePayload`

`copyCustomModuleFormPayload`

`copyCustomModulePayload`

`copyOfferingPayload`

`createAcceptedInsurancePlanPayload`

`createAddendumPayload`

`createAllergySensitivityPayload`

`createAnnouncementPayload`

`createApiKeyPayload`

`createAppleHealthPayload`

`createAppointmentFormAnswerGroupConnectionPayload`

`createAppointmentPayload`

`createAppointmentRequestPayload`

`createAppointmentSettingPayload`

`createAppointmentTypeCptCodePayload`

`createAppointmentTypePayload`

`createAutoTaskGeneratorPayload`

`createAutomatedInsuranceBillingSettingPayload`

`createAvailabilityPayload`

`createBillingItemPayload`

`createBrandPayload`

`createCarePlanPayload`

`createCarePlanRecommendationCategoryPayload`

`createChatSettingPayload`

`createClientPayload`

`createClientRestrictionAuthorizationPayload`

`createCms1500Payload`

`createCognitiveStatusPayload`

`createCommentPayload`

`createCompletedCourseItemPayload`

`createCompletedOnboardingItemPayload`

`createContactPayload`

`createConversationPayload`

`createCourseBenefitPayload`

`createCourseItemPayload`

`createCoursePayload`

`createCustomEmailPayload`

`createCustomFoodPayload`

`createCustomModuleFormPayload`

`createCustomModulePayload`

`createDocumentPayload`

`createDosespotClinicianPayload`

`createDraftPayload`

`createDsiCommentPayload`

`createEbookPayload`

`createEntryPayload`

`createEpisodeOfCarePayload`

`createExternalCalendarPayload`

`createFamilyHistoryPayload`

`createFaxAcctInfoPayload`

`createFaxLineRequestPayload`

`createFeatureTogglePayload`

`createFitbitPayload`

`createFolderPayload`

`createFormAnswerFileAttachmentPayload`

`createFormAnswerFileAttachmentUploadUrlPayload`

`createFormAnswerGroupPayload`

`createFormAnswerGroupSigningPayload`

`createFullscriptPractitionerPayload`

`createFunctionalStatusPayload`

`createGoalHistoryPayload`

`createGoalPayload`

`createGoogleFitPayload`

`createGroupPayload`

`createHealthConcernPayload`

`createImmunizationPayload`

`createImplantableDeviceUserPayload`

`createImportDataRequestPayload`

`createInsuranceAuthorizationPayload`

`createInsurancePaymentPayload`

`createInsurancePlanPayload`

`createLabOrderPayload`

`createLocationPayload`

`createMealPayload`

`createMedicationPayload`

`createMessageBlastPayload`

`createNotePayload`

`createNotificationContactPayload`

`createOfferingCouponPayload`

`createOfferingPayload`

`createOfficeallySftpAccountPayload`

`createOnboardingFlowPayload`

`createOnboardingItemPayload`

`createOrAddToWaterIntakeEntryPayload`

`createOrganizationCptCodePayload`

`createOrganizationMembershipPayload`

`createOrganizationPayload`

`createPartnerPayload`

`createPaymentIntentPayload`

`createPdfLetterheadTemplatePayload`

`createPermissionTemplatePayload`

`createPersonalizationQuestionnairePayload`

`createPreferredMedicalCodePayload`

`createProcedurePayload`

`createProductPayload`

`createProviderAcceptedInsurancePlansPayload`

`createProviderCptCodesPayload`

`createRecommendationPayload`

`createReferralPayload`

`createReferringPhysicianPayload`

`createRequestedFormPayload`

`createRequestedPaymentPayload`

`createRupaOrderPayload`

`createSavedFilterPayload`

`createSentDirectMessagePayload`

`createSentFaxPayload`

`createSetupIntentPayload`

`createSmartPhrasePayload`

`createSmokingStatusPayload`

`createStripeCustomerDetailPayload`

`createSubscriptionPayload`

`createSuperBillPayload`

`createTagPayload`

`createTaskPayload`

`createUniqueDeviceIdentifierPayload`

`createVisitorPayload`

`createWebhookPayload`

`createWriteOffPayload`

`deleteAcceptedInsurancePlanPayload`

`deleteAllergySensitivityPayload`

`deleteApiKeyPayload`

`deleteAppleHealthPayload`

`deleteAppointmentFormAnswerGroupConnectionPayload`

`deleteAppointmentPayload`

`deleteAppointmentRequestPayload`

`deleteAppointmentTypeCptCodePayload`

`deleteAppointmentTypePayload`

`deleteAutoTaskGeneratorPayload`

`deleteAvailabilityPayload`

`deleteBillingItemPayload`

`deleteCarePlanConnectionPayload`

`deleteCarePlanPayload`

`deleteCarePlanRecommendationCategoryPayload`

`deleteClientRestrictionAuthorizationPayload`

`deleteCms1500Payload`

`deleteCognitiveStatusPayload`

`deleteCommentPayload`

`deleteConversationMembershipPayload`

`deleteCourseBenefitPayload`

`deleteCourseGroupPayload`

`deleteCourseItemPayload`

`deleteCourseMembershipPayload`

`deleteCoursePayload`

`deleteCustomEmailPayload`

`deleteCustomFoodPayload`

`deleteCustomModuleFormPayload`

`deleteCustomModulePayload`

`deleteDexcomConnectionPayload`

`deleteDocumentPayload`

`deleteEntryPayload`

`deleteEpisodeOfCarePayload`

`deleteExternalCalendarPayload`

`deleteFamilyHistoryPayload`

`deleteFitbitPayload`

`deleteFolderPayload`

`deleteFormAnswerFileAttachmentPayload`

`deleteFormAnswerGroupPayload`

`deleteFormAnswerGroupSigningPayload`

`deleteFunctionalStatusPayload`

`deleteGoalHistoryPayload`

`deleteGoalPayload`

`deleteGoogleFitPayload`

`deleteHealthConcernPayload`

`deleteImplantableDeviceUserPayload`

`deleteInsuranceAuthorizationPayload`

`deleteInsurancePlanPayload`

`deleteLocationPayload`

`deleteManualInsurancePaymentPayload`

`deleteMealPayload`

`deleteNotePayload`

`deleteNotificationContactPayload`

`deleteOfferingCouponPayload`

`deleteOfferingPayload`

`deleteOnboardingFlowPayload`

`deleteOnboardingItemPayload`

`deleteOrganizationCptCodePayload`

`deleteOrganizationInfoPayload`

`deleteOrganizationMembershipPayload`

`deletePermissionTemplatePayload`

`deletePreferredMedicalCodePayload`

`deleteProcedurePayload`

`deleteProductPayload`

`deleteProviderAcceptedInsurancePlanPayload`

`deleteProviderCptCodePayload`

`deleteReceivedFaxPayload`

`deleteRecommendationPayload`

`deleteReferralPayload`

`deleteReferringPhysicianPayload`

`deleteRequestedFormPayload`

`deleteRequestedPaymentPayload`

`deleteSavedFilterPayload`

`deleteShapaConnectionPayload`

`deleteSmartPhrasePayload`

`deleteSmokingStatusPayload`

`deleteStripeCustomerDetailPayload`

`deleteSuperBillPayload`

`deleteTagPayload`

`deleteTaskPayload`

`deleteUniqueDeviceIdentifierPayload`

`deleteUserGroupPayload`

`deleteWebhookPayload`

`deleteWithingsConnectionPayload`

`deleteWriteOffPayload`

`deleteZoomRecordingFilePayload`

`destroyAnnouncementPayload`

`destroyFaxAcctInfoPayload`

`destroyMedicationPayload`

`destroyPdfLetterheadTemplatePayload`

`destroyRecurringFormPayload`

`dismissAllAnnouncementsPayload`

`dismissAnnouncementPayload`

`editAvailabilityPayload`

`expireWebhookSignaturePayload`

`exportClientEhiPayload`

`exportToTemplatePayload`

`fullscript`

`generateChartingPdfPayload`

`ingestMedicationsFromSurescriptsPayload`

`linkEncounterToEpisodeOfCarePayload`

`logMedicationHistoryConsentPayload`

`mergeClientsPayload`

`parseCcdaDocumentPayload`

`rejectGeneratedFormAnswerGroupPayload`

`removeAppliedTagPayload`

`removeDraftPayload`

`removeUserFromGroupCarePlanPayload`

`resendSentFaxPayload`

`resetDefaultPdfLetterheadTemplatePayload`

`resetPasswordPayload`

`resyncRupaLabOrdersPayload`

`revokeTokenPayload`

`runEligibilityCheckMutationPayload`

`sendCarePlanEmailPayload`

`sendTestWebhookPayload`

`setDefaultPdfLetterheadTemplatePayload`

`shareAnswersAsDocumentPayload`

`shareCoursePayload`

`shareCustomModuleFormPayload`

`signInPayload`

`signUpPayload`

`toggleCarePlanStatusForSpecificUserPayload`

`unlinkEncounterToEpisodeOfCarePayload`

`unsubscribeFromNotificationPayload`

`updateAddendumPayload`

`updateAllergySensitivityPayload`

`updateAnnouncementPayload`

`updateAppleHealthPayload`

`updateAppointmentInclusionPayload`

`updateAppointmentPayload`

`updateAppointmentRequestPayload`

`updateAppointmentSettingPayload`

`updateAppointmentTypeCptCodePayload`

`updateAppointmentTypePayload`

`updateAutoTaskGeneratorPayload`

`updateAutomatedInsuranceBillingSettingPayload`

`updateBillingItemPayload`

`updateBrandPayload`

`updateByTemplatePayload`

`updateCalendarViewSettingPayload`

`updateCarePlanPayload`

`updateCarePlanRecommendationCategoryPayload`

`updateChangeHealthAccountPayload`

`updateChargeBackPayload`

`updateChatSettingPayload`

`updateClientPayload`

`updateCms1500Payload`

`updateCognitiveStatusPayload`

`updateConversationMembershipPayload`

`updateConversationPayload`

`updateCourseGroupPayload`

`updateCourseItemPayload`

`updateCourseMembershipPayload`

`updateCoursePayload`

`updateCustomEmailPayload`

`updateCustomFoodPayload`

`updateCustomModuleFormPayload`

`updateCustomModulePayload`

`updateDocumentPayload`

`updateDsiCommentPayload`

`updateEntryPayload`

`updateEpisodeOfCarePayload`

`updateExternalCalendarPayload`

`updateFamilyHistoryPayload`

`updateFaxAcctInfoPayload`

`updateFeatureTogglePayload`

`updateFitbitPayload`

`updateFolderPayload`

`updateFormAnswerGroupPayload`

`updateFunctionalStatusPayload`

`updateGeneratedFormAnswerGroupFeedbackPayload`

`updateGoalPayload`

`updateGoogleFitPayload`

`updateGroupCarePlanPayload`

`updateHealthConcernPayload`

`updateHumanPayload`

`updateImmunizationPayload`

`updateImplantableDeviceUserPayload`

`updateInsuranceAuthorizationPayload`

`updateInsurancePaymentDepositStatusPayload`

`updateInsurancePlanPayload`

`updateLabOrderPayload`

`updateLocationPayload`

`updateManualInsurancePaymentPayload`

`updateMealPayload`

`updateMedicationPayload`

`updateNotePayload`

`updateNoteSchedulerPayload`

`updateNotificationContactPayload`

`updateNotificationPayload`

`updateNotificationSettingPayload`

`updateOfferingPayload`

`updateOfficeallySftpAccountPayload`

`updateOnboardingFlowPayload`

`updateOnboardingItemPayload`

`updateOrganizationCptCodePayload`

`updateOrganizationMemberPayload`

`updateOrganizationMembershipPayload`

`updateOrganizationPayload`

`updatePdfLetterheadTemplatePayload`

`updatePermissionTemplatePayload`

`updatePolicyMutationPayload`

`updateProcedurePayload`

`updateProductPayload`

`updateProviderCptCodesPayload`

`updateReceivedDirectMessagePayload`

`updateReceivedFaxPayload`

`updateRecommendationPayload`

`updateRecurringFormPayload`

`updateReferralPayload`

`updateReferringPhysicianPayload`

`updateRequestedPaymentPayload`

`updateSavedFilterPayload`

`updateSmartPhrasePayload`

`updateSmokingStatusPayload`

`updateStatePayload`

`updateStripeCustomerDetailPayload`

`updateStripeVerificationDetailsPayload`

`updateSubscriptionPayload`

`updateSuperBillPayload`

`updateTagPayload`

`updateTaskPayload`

`updateUniqueDeviceIdentifierPayload`

`updateUserAppointmentPricingPayload`

`updateUserGroupPayload`

`updateUserPayload`

`updateWebhookPayload`

`updateWriteOffPayload`

`uploadBatchToCandidHealthPayload`

`uploadBatchToChangeHealthPayload`

`uploadBatchToOfficeallyPayload`

`uploadToIntegrationsPayload`

`validateVerificationTokenPayload`

## Input Objects

`AddedUsersInput`

`AdvanceAppointmentPriceInput`

`AdvanceAppointmentPricesInput`

`AnnouncementImageUpload`

`AppointmentAutocompleteFormCreateInput`

`AppointmentAutocompleteFormUpdateInput`

`AppointmentLocationInput`

`AppointmentRequestSlotInput`

`AppointmentTypeAppointmentSettingInput`

`AppointmentTypeCptCode`

`AppointmentTypeCreditInput`

`AppointmentTypeFormConnectionInput`

`AttendedClientsInput`

`AvailabilityInput`

`BenefitInput`

`BillingAddressInput`

`BulkDeleteAvailabilityInput`

`BulkEntryInput`

`CalendarColorSchemeInput`

`CallReferenceInput`

`CancelMobileHealthDataSnapshotInput`

`CancellationReasonOptionInput`

`ChangeDevicesAvailabilityInput`

`ChargeBackEvidenceInput`

`CheckoutFormAnswerGroupInput`

`CheckoutFormAnswerInput`

`ClaimCobOverridesInput`

`ClaimLineCobOverridesInput`

`ClientInsurancePlanInput`

`ClientLocationInput`

`ClientPolicyInput`

`ClientPortalSettingInput`

`ClientSourceInput`

`Cms1500PolicyInput`

`Cms1500ReferringPhysicianInput`

`CobAdjustmentInput`

`ColorCodeInput`

`CompleteCcdaReconciliationInput`

`ContactTypeOverride`

`ContactTypeOverrideInput`

`CourseMembersInput`

`CptCodesCms1500Input`

`CptCodesPolicyInput`

`CptCodesSuperBillInput`

`CreateAvailabilityWithAppointmentTypesInput`

`CreateChangeHealthPatientInput`

`CreateClientViaFormInput`

`CreateCustomModuleFileAttachmentInput`

`CreateCustomModuleFileAttachmentUploadUrlInput`

`CreateInternalCommentInput`

`CreateMobileHealthDataIntegrationInput`

`CreateMobileHealthDataSnapshotInput`

`CreateSecondaryClaimInput`

`CreateSharingsInput`

`CustomMetricInput`

`CustomMetricOverridesInput`

`CustomModuleConditionInput`

`DayRangeInputObjectType`

`DeleteCustomModuleFileAttachmentInput`

`DeleteMobileHealthDataIntegrationInput`

`DeleteTranscriptInput`

`DestroyInternalCommentInput`

`DestroySharingsInput`

`DiagnosesInput`

`DietitianInput`

`EditAvailabilityWithAppointmentTypesInput`

`FaxDietitianInput`

`FaxLocationInput`

`FormAnswerInput`

`GiftInput`

`HealthAssessmentServiceSignupInput`

`IcdCodesCms1500Input`

`IcdCodesIndividualClientNoteInput`

`IcdCodesPolicyInput`

`IcdCodesSuperBillInput`

`IndividualClientNoteInput`

`InsuranceAuthorizationInput`

`InsurancePlanInput`

`LabObservationRequestInput`

`LabObservationResultInput`

`LocationInput`

`LocationInputs`

`LockInput`

`NoteInput`

`NotificationContactInput`

`NutrientsInput`

`OfferingImageUpload`

`OfferingIncludesFields`

`OfferingProductInput`

`OrgLocationInput`

`OrganizationCptCodeInsuranceFeesInput`

`OrganizationInfoInput`

`OrganizationSettingsInput`

`OtherIdNumberInput`

`PatientInput`

`PatientLocationInputs`

`PauseCourseGroupInput`

`PauseCourseMembershipInput`

`PhysicianLocationInput`

`PhysicianReferralInput`

`PolicyInput`

`PrescriptionMedicationQueryFiltersInput`

`PrimaryOrganizationInfoInput`

`ProcessMobileHealthDataSnapshotInput`

`ProductInput`

`ProfessionsInput`

`ProviderAppointmentLocationsInput`

`ProviderBioInput`

`ProviderCptCodeInput`

`ReceiptLineItemInput`

`RecurringAppointmentInput`

`RecurringDaysInputObjectType`

`ReferralInfoInput`

`ReferralInput`

`ReferringPhysicianInput`

`RefetchChangeHealthLabOrderInput`

`ReminderInput`

`RequestIntegrationInput`

`RequestedPayerInput`

`RequestedPaymentTemplateInput`

`ResetMfaInput`

`ResumeCourseGroupInput`

`ResumeCourseMembershipInput`

`RoomInput`

`SendSpeakToTrainerNotificationInput`

`ServingSizeInput`

`SetCustomModuleFormScribeInstructionsInput`

`SignInput`

`SpecialtiesInput`

`StateLicensesInput`

`SubOrganizationInfoInput`

`SubentryInput`

`SubgoalInput`

`SubmissionInput`

`SubmitSecondaryClaimInput`

`TaskReminderInput`

`TestInput`

`UnlockInput`

`UpdateCalorieLevelInput`

`UpdateInternalCommentInput`

`UpdateMacronutrientSplitInput`

`UpdateSecondaryClaimInput`

`UpdateUiConfigurationInput`

`UserPolicyInput`

`VideoUrlDefaultInput`

`VideoUrlOptionInput`

`WebhookEventInput`

`WriteOffInput`

`addPharmacyInput`

`asyncBulkCreateOrganizationMembershipsInput`

`bulkApplyCarePlanTemplateInput`

`bulkApplyInput`

`bulkCreateAvailabilityInput`

`bulkCreateEntriesInput`

`bulkCreateOrganizationMembershipsInput`

`bulkDeleteTasksInput`

`bulkUpdateCardIssuesInput`

`bulkUpdateCarePlanUsersInput`

`bulkUpdateClientsInput`

`bulkUpdateNotificationRecordsInput`

`bulkUpdateNotificationsInput`

`bulkUpdateTasksInput`

`cancelRecurringPaymentInput`

`clearUnreconciledObjectsInput`

`completeCheckoutInput`

`completeCourseDocumentInput`

`convertGeneratedFormAnswerGroupInput`

`copyCourseInput`

`copyCustomModuleFormInput`

`copyCustomModuleInput`

`copyOfferingInput`

`createAcceptedInsurancePlanInput`

`createAddendumInput`

`createAllergySensitivityInput`

`createAnnouncementInput`

`createApiKeyInput`

`createAppleHealthInput`

`createAppointmentFormAnswerGroupConnectionInput`

`createAppointmentInput`

`createAppointmentRequestInput`

`createAppointmentSettingInput`

`createAppointmentTypeCptCodeInput`

`createAppointmentTypeInput`

`createAutoTaskGeneratorInput`

`createAutomatedInsuranceBillingSettingInput`

`createAvailabilityInput`

`createBillingItemInput`

`createBrandInput`

`createCarePlanInput`

`createCarePlanRecommendationCategoryInput`

`createChatSettingInput`

`createClientInput`

`createClientRestrictionAuthorizationInput`

`createCms1500Input`

`createCognitiveStatusInput`

`createCommentInput`

`createCompletedCourseItemInput`

`createCompletedOnboardingItemInput`

`createContactInput`

`createConversationInput`

`createCourseBenefitInput`

`createCourseInput`

`createCourseItemInput`

`createCustomEmailInput`

`createCustomFoodInput`

`createCustomModuleFormInput`

`createCustomModuleInput`

`createDocumentInput`

`createDosespotClinicianInput`

`createDraftInput`

`createDsiCommentInput`

`createEbookInput`

`createEntryInput`

`createEpisodeOfCareInput`

`createExternalCalendarInput`

`createFamilyHistoryInput`

`createFaxAcctInfoInput`

`createFaxLineRequestInput`

`createFeatureToggleInput`

`createFitbitInput`

`createFolderInput`

`createFormAnswerFileAttachmentInput`

`createFormAnswerFileAttachmentUploadUrlInput`

`createFormAnswerGroupInput`

`createFormAnswerGroupSigningInput`

`createFullscriptPractitionerInput`

`createFunctionalStatusInput`

`createGoalHistoryInput`

`createGoalInput`

`createGoogleFitInput`

`createGroupInput`

`createHealthConcernInput`

`createImmunizationInput`

`createImplantableDeviceUserInput`

`createImportDataRequestInput`

`createInsuranceAuthorizationInput`

`createInsurancePaymentInput`

`createInsurancePlanInput`

`createLabOrderInput`

`createLocationInput`

`createMealInput`

`createMedicationInput`

`createMessageBlastInput`

`createNoteInput`

`createNotificationContactInput`

`createOfferingCouponInput`

`createOfferingInput`

`createOfficeallySftpAccountInput`

`createOnboardingFlowInput`

`createOnboardingItemInput`

`createOrAddToWaterIntakeEntryInput`

`createOrganizationCptCodeInput`

`createOrganizationInput`

`createOrganizationMembershipInput`

`createPartnerInput`

`createPaymentIntentInput`

`createPdfLetterheadTemplateInput`

`createPermissionTemplateInput`

`createPersonalizationQuestionnaireInput`

`createPreferredMedicalCodeInput`

`createProcedureInput`

`createProductInput`

`createProviderAcceptedInsurancePlansInput`

`createProviderCptCodesInput`

`createRecommendationInput`

`createReferralInput`

`createReferringPhysicianInput`

`createRequestedFormInput`

`createRequestedPaymentInput`

`createRupaOrderInput`

`createSavedFilterInput`

`createSentDirectMessageInput`

`createSentFaxInput`

`createSetupIntentInput`

`createSmartPhraseInput`

`createSmokingStatusInput`

`createStripeCustomerDetailInput`

`createSubscriptionInput`

`createSuperBillInput`

`createTagInput`

`createTaskInput`

`createUniqueDeviceIdentifierInput`

`createVisitorInput`

`createWebhookInput`

`createWriteOffInput`

`deleteAcceptedInsurancePlanInput`

`deleteAllergySensitivityInput`

`deleteApiKeyInput`

`deleteAppleHealthInput`

`deleteAppointmentFormAnswerGroupConnectionInput`

`deleteAppointmentInput`

`deleteAppointmentRequestInput`

`deleteAppointmentTypeCptCodeInput`

`deleteAppointmentTypeInput`

`deleteAutoTaskGeneratorInput`

`deleteAvailabilityInput`

`deleteBillingItemInput`

`deleteCarePlanConnectionInput`

`deleteCarePlanInput`

`deleteCarePlanRecommendationCategoryInput`

`deleteClientRestrictionAuthorizationInput`

`deleteCms1500Input`

`deleteCognitiveStatusInput`

`deleteCommentInput`

`deleteConversationMembershipInput`

`deleteCourseBenefitInput`

`deleteCourseGroupInput`

`deleteCourseInput`

`deleteCourseItemInput`

`deleteCourseMembershipInput`

`deleteCustomEmailInput`

`deleteCustomFoodInput`

`deleteCustomModuleFormInput`

`deleteCustomModuleInput`

`deleteDexcomConnectionInput`

`deleteDocumentInput`

`deleteEntryInput`

`deleteEpisodeOfCareInput`

`deleteExternalCalendarInput`

`deleteFamilyHistoryInput`

`deleteFitbitInput`

`deleteFolderInput`

`deleteFormAnswerFileAttachmentInput`

`deleteFormAnswerGroupInput`

`deleteFormAnswerGroupSigningInput`

`deleteFunctionalStatusInput`

`deleteGoalHistoryInput`

`deleteGoalInput`

`deleteGoogleFitInput`

`deleteHealthConcernInput`

`deleteImplantableDeviceUserInput`

`deleteInsuranceAuthorizationInput`

`deleteInsurancePlanInput`

`deleteLocationInput`

`deleteManualInsurancePaymentInput`

`deleteMealInput`

`deleteNoteInput`

`deleteNotificationContactInput`

`deleteOfferingCouponInput`

`deleteOfferingInput`

`deleteOnboardingFlowInput`

`deleteOnboardingItemInput`

`deleteOrganizationCptCodeInput`

`deleteOrganizationInfoInput`

`deleteOrganizationMembershipInput`

`deletePermissionTemplateInput`

`deletePreferredMedicalCodeInput`

`deleteProcedureInput`

`deleteProductInput`

`deleteProviderAcceptedInsurancePlanInput`

`deleteProviderCptCodeInput`

`deleteReceivedFaxInput`

`deleteRecommendationInput`

`deleteReferralInput`

`deleteReferringPhysicianInput`

`deleteRequestedFormInput`

`deleteRequestedPaymentInput`

`deleteSavedFilterInput`

`deleteShapaConnectionInput`

`deleteSmartPhraseInput`

`deleteSmokingStatusInput`

`deleteStripeCustomerDetailInput`

`deleteSuperBillInput`

`deleteTagInput`

`deleteTaskInput`

`deleteUniqueDeviceIdentifierInput`

`deleteUserGroupInput`

`deleteWebhookInput`

`deleteWithingsConnectionInput`

`deleteWriteOffInput`

`deleteZoomRecordingFileInput`

`destroyAnnouncementInput`

`destroyFaxAcctInfoInput`

`destroyMedicationInput`

`destroyPdfLetterheadTemplateInput`

`destroyRecurringFormInput`

`dismissAllAnnouncementsInput`

`dismissAnnouncementInput`

`editAvailabilityInput`

`expireWebhookSignatureInput`

`exportClientEhiInput`

`exportToTemplateInput`

`generateChartingPdfInput`

`ingestMedicationsFromSurescriptsInput`

`linkEncounterToEpisodeOfCareInput`

`logMedicationHistoryConsentInput`

`mergeClientsInput`

`parseCcdaDocumentInput`

`rejectGeneratedFormAnswerGroupInput`

`removeAppliedTagInput`

`removeDraftInput`

`removeUserFromGroupCarePlanInput`

`resendSentFaxInput`

`resetDefaultPdfLetterheadTemplateInput`

`resetPasswordInput`

`resyncRupaLabOrdersInput`

`revokeTokenInput`

`runEligibilityCheckMutationInput`

`sendCarePlanEmailInput`

`sendTestWebhookInput`

`setDefaultPdfLetterheadTemplateInput`

`shareAnswersAsDocumentInput`

`shareCourseInput`

`shareCustomModuleFormInput`

`signInInput`

`signUpInput`

`toggleCarePlanStatusForSpecificUserInput`

`unlinkEncounterToEpisodeOfCareInput`

`unsubscribeFromNotificationInput`

`updateAddendumInput`

`updateAllergySensitivityInput`

`updateAnnouncementInput`

`updateAppleHealthInput`

`updateAppointmentInclusionInput`

`updateAppointmentInput`

`updateAppointmentRequestInput`

`updateAppointmentSettingInput`

`updateAppointmentTypeCptCodeInput`

`updateAppointmentTypeInput`

`updateAutoTaskGeneratorInput`

`updateAutomatedInsuranceBillingSettingInput`

`updateBillingItemInput`

`updateBrandInput`

`updateByTemplateInput`

`updateCalendarViewSettingInput`

`updateCarePlanInput`

`updateCarePlanRecommendationCategoryInput`

`updateChangeHealthAccountInput`

`updateChargeBackInput`

`updateChatSettingInput`

`updateClientInput`

`updateCms1500Input`

`updateCognitiveStatusInput`

`updateConversationInput`

`updateConversationMembershipInput`

`updateCourseGroupInput`

`updateCourseInput`

`updateCourseItemInput`

`updateCourseMembershipInput`

`updateCustomEmailInput`

`updateCustomFoodInput`

`updateCustomModuleFormInput`

`updateCustomModuleInput`

`updateDocumentInput`

`updateDsiCommentInput`

`updateEntryInput`

`updateEpisodeOfCareInput`

`updateExternalCalendarInput`

`updateFamilyHistoryInput`

`updateFaxAcctInfoInput`

`updateFeatureToggleInput`

`updateFitbitInput`

`updateFolderInput`

`updateFormAnswerGroupInput`

`updateFunctionalStatusInput`

`updateGeneratedFormAnswerGroupFeedbackInput`

`updateGoalInput`

`updateGoogleFitInput`

`updateGroupCarePlanInput`

`updateHealthConcernInput`

`updateHumanInput`

`updateImmunizationInput`

`updateImplantableDeviceUserInput`

`updateInsuranceAuthorizationInput`

`updateInsurancePaymentDepositStatusInput`

`updateInsurancePlanInput`

`updateLabOrderInput`

`updateLocationInput`

`updateManualInsurancePaymentInput`

`updateMealInput`

`updateMedicationInput`

`updateNoteInput`

`updateNoteSchedulerInput`

`updateNotificationContactInput`

`updateNotificationInput`

`updateNotificationSettingInput`

`updateOfferingInput`

`updateOfficeallySftpAccountInput`

`updateOnboardingFlowInput`

`updateOnboardingItemInput`

`updateOrganizationCptCodeInput`

`updateOrganizationInput`

`updateOrganizationMemberInput`

`updateOrganizationMembershipInput`

`updatePdfLetterheadTemplateInput`

`updatePermissionTemplateInput`

`updatePolicyMutationInput`

`updateProcedureInput`

`updateProductInput`

`updateProviderCptCodesInput`

`updateReceivedDirectMessageInput`

`updateReceivedFaxInput`

`updateRecommendationInput`

`updateRecurringFormInput`

`updateReferralInput`

`updateReferringPhysicianInput`

`updateRequestedPaymentInput`

`updateSavedFilterInput`

`updateSmartPhraseInput`

`updateSmokingStatusInput`

`updateStateInput`

`updateStripeCustomerDetailInput`

`updateStripeVerificationDetailsInput`

`updateSubscriptionInput`

`updateSuperBillInput`

`updateTagInput`

`updateTaskInput`

`updateUniqueDeviceIdentifierInput`

`updateUserAppointmentPricingInput`

`updateUserGroupInput`

`updateUserInput`

`updateWebhookInput`

`updateWriteOffInput`

`uploadBatchToCandidHealthInput`

`uploadBatchToChangeHealthInput`

`uploadBatchToOfficeallyInput`

`uploadToIntegrationsInput`

`validateVerificationTokenInput`

## Enums

`Action`

`ActiveCareTeamMemberOrderKeys`

`AdjustmentGroup`

`AllergySensitivityCategory`

`AllergySensitivityCategoryType`

`AllergySensitivityReactionType`

`AllergySensitivitySeverity`

`AllergySensitivityStatus`

`ApiKeyOrderKeys`

`AppliedTagOrderKeys`

`AppointmentOrderKeys`

`AppointmentPricingMethod`

`AppointmentRequestOrderKeys`

`AppointmentRequestStatus`

`AppointmentTypeOrderKeys`

`AppointmentWorkflowChartNoteStatus`

`AuditEventOrderKeys`

`AuditEventResourceName`

`AuditEventType`

`BaseCalendarInterval`

`BillingItemOrderKeys`

`BillingItemState`

`CalendarStatus`

`CalendarType`

`CancellationReasonTypeEnum`

`CarePlanOrderKeys`

`ChargeBackOrderKeys`

`ChargeDisputeStatus`

`ChartNoteStatus`

`ClaimDestinationIntegration`

`ClaimMdRejectionMessagesInfo`

`ClaimPolicyPriority`

`Cms1500OrderKeys`

`Cms1500Status`

`ConversationMembershipOrderKeys`

`CourseMembershipStatus`

`CourseType`

`CourseTypeFilter`

`CustomModuleFormOrderKeys`

`DefaultBillingType`

`DocumentOrderKeys`

`DrugAllergenTypeEnum`

`EligibilityCheckService`

`EntryImageStyleEnum`

`EntryOrderKeys`

`EthnicityCode`

`FolderOrderKeys`

`FormAnswerGroupOrderKeys`

`FormHistoryAction`

`FormHistorySourceable`

`FormStatus`

`FormType`

`FullscriptEntrypoint`

`GenderIdentityCode`

`GeneratedFormAnswerGroupRejectionReasonEnum`

`GoalHistoryActionTypeEnum`

`GoalOrderKeys`

`HolderRelationship`

`IcdCodeOrderKeys`

`IndividualClientNoteOrderKeys`

`IndividualClientNoteSorting`

`InsurancePaymentsDepositStatusEnum`

`InsurancePaymentsOrderKeys`

`InsurancePlanOrderKeys`

`IntakeFlowOrderKeys`

`IntegrationPlanTiersType`

`InternalCommentable`

`InternalCommentsOrderKeys`

`InterventionType`

`LabOrderBilling`

`LabOrderIntegration`

`LabOrderInterpretation`

`LabOrderLabVendor`

`LabOrderOrderKeys`

`MfaType`

`MobileHealthDataIntegrationType`

`MobileHealthDataSnapshotIntegrationType`

`MobileHealthDataSnapshotStatus`

`MonographFormat`

`NoteOrderKeys`

`NotificationOrderKeys`

`OfferingCouponOrderKeys`

`OfferingOrderKeys`

`OnboardingFlowOrderKeys`

`OrganizationMembershipOrderKeys`

`OrganizationMembershipRole`

`PartnerType`

`PayerOrder`

`PdfLetterheadTemplateAddressSource`

`PdfLetterheadTemplateBrandLogoSource`

`PdfLetterheadTemplateEmailSource`

`PdfLetterheadTemplatePhoneNumberSource`

`PdfLetterheadTemplateTeamMemberNameSource`

`PharmacySpecialty`

`PrescriptionMedicationOrderBy`

`PrescriptionMedicationStatus`

`PrescriptionMedicationTypeEnum`

`ProductOrderKeys`

`RaceCode`

`ReceivedDirectMessageOrderKeys`

`ReceivedFaxOrderKeys`

`ReferringPhysicianOrderKeys`

`RequestedPaymentOrderKeys`

`RequestedPaymentStatus`

`SentDirectMessageOrderKeys`

`SentDirectMessageXml`

`SentFaxOrderKeys`

`SentWebhookOrderKeys`

`SentWebhookResourceType`

`ShareableType`

`SignedStreamName`

`SmartPhraseOrderKeys`

`States`

`StripeCustomerDetailOrderKeys`

`SuperBillOrderKeys`

`TagOrderKeys`

`TaskOrderKeys`

`TranscriptStatusEnum`

`TranscriptTypeEnum`

`TransferOrderKeys`

`UserGroupOrderKeys`

`UserOrderKeys`

`WebhookEventType`

`WebhookOrderKeys`

`WriteOffType`

`ZoomRecordingFileTypeEnum`

`ZoomRecordingStatusEnum`

`ZoomRecordingTypeEnum`

## Unions

`CustomEmailRelatedObject`

`PrescriptionMedication`

`RelatedObjectUnion`

`Shareable`

## Scalars

`Boolean`

`Cursor`

`Float`

`HexColor`

`ID`

`ISO8601Date`

`ISO8601DateTime`

`ISO8601Duration`

`Int`

`JSON`

`String`

`UUID`

`Upload`

## Directives

`deprecated`

`feature`

`include`

`oneOf`

`skip`

`specifiedBy`

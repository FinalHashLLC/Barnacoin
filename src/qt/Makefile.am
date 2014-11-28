include $(top_srcdir)/src/Makefile.include

AM_CPPFLAGS += -I$(top_srcdir)/src \
  -I$(top_builddir)/src/qt \
  -I$(top_builddir)/src/qt/forms \
  $(PROTOBUF_CFLAGS) \
  $(QR_CFLAGS)
bin_PROGRAMS = barnacoin-qt
noinst_LIBRARIES = libbarnacoinqt.a
SUBDIRS = . $(BUILD_TEST_QT)
DIST_SUBDIRS = . test

# barnacoin qt core #
QT_TS = \
  locale/barnacoin_ach.ts \
  locale/barnacoin_af_ZA.ts \
  locale/barnacoin_ar.ts \
  locale/barnacoin_be_BY.ts \
  locale/barnacoin_bg.ts \
  locale/barnacoin_bs.ts \
  locale/barnacoin_ca_ES.ts \
  locale/barnacoin_ca.ts \
  locale/barnacoin_ca@valencia.ts \
  locale/barnacoin_cmn.ts \
  locale/barnacoin_cs.ts \
  locale/barnacoin_cy.ts \
  locale/barnacoin_da.ts \
  locale/barnacoin_de.ts \
  locale/barnacoin_el_GR.ts \
  locale/barnacoin_en.ts \
  locale/barnacoin_eo.ts \
  locale/barnacoin_es_CL.ts \
  locale/barnacoin_es_DO.ts \
  locale/barnacoin_es_MX.ts \
  locale/barnacoin_es.ts \
  locale/barnacoin_es_UY.ts \
  locale/barnacoin_et.ts \
  locale/barnacoin_eu_ES.ts \
  locale/barnacoin_fa_IR.ts \
  locale/barnacoin_fa.ts \
  locale/barnacoin_fi.ts \
  locale/barnacoin_fr_CA.ts \
  locale/barnacoin_fr.ts \
  locale/barnacoin_gl.ts \
  locale/barnacoin_gu_IN.ts \
  locale/barnacoin_he.ts \
  locale/barnacoin_hi_IN.ts \
  locale/barnacoin_hr.ts \
  locale/barnacoin_hu.ts \
  locale/barnacoin_id_ID.ts \
  locale/barnacoin_it.ts \
  locale/barnacoin_ja.ts \
  locale/barnacoin_ka.ts \
  locale/barnacoin_kk_KZ.ts \
  locale/barnacoin_ko_KR.ts \
  locale/barnacoin_ky.ts \
  locale/barnacoin_la.ts \
  locale/barnacoin_lt.ts \
  locale/barnacoin_lv_LV.ts \
  locale/barnacoin_mn.ts \
  locale/barnacoin_ms_MY.ts \
  locale/barnacoin_nb.ts \
  locale/barnacoin_nl.ts \
  locale/barnacoin_pam.ts \
  locale/barnacoin_pl.ts \
  locale/barnacoin_pt_BR.ts \
  locale/barnacoin_pt_PT.ts \
  locale/barnacoin_ro_RO.ts \
  locale/barnacoin_ru.ts \
  locale/barnacoin_sah.ts \
  locale/barnacoin_sk.ts \
  locale/barnacoin_sl_SI.ts \
  locale/barnacoin_sq.ts \
  locale/barnacoin_sr.ts \
  locale/barnacoin_sv.ts \
  locale/barnacoin_th_TH.ts \
  locale/barnacoin_tr.ts \
  locale/barnacoin_uk.ts \
  locale/barnacoin_ur_PK.ts \
  locale/barnacoin_uz@Cyrl.ts \
  locale/barnacoin_vi.ts \
  locale/barnacoin_vi_VN.ts \
  locale/barnacoin_zh_CN.ts \
  locale/barnacoin_zh_HK.ts \
  locale/barnacoin_zh_TW.ts

QT_FORMS_UI = \
  forms/aboutdialog.ui \
  forms/addressbookpage.ui \
  forms/askpassphrasedialog.ui \
  forms/coincontroldialog.ui \
  forms/editaddressdialog.ui \
  forms/helpmessagedialog.ui \
  forms/intro.ui \
  forms/openuridialog.ui \
  forms/optionsdialog.ui \
  forms/overviewpage.ui \
  forms/receivecoinsdialog.ui \
  forms/receiverequestdialog.ui \
  forms/rpcconsole.ui \
  forms/sendcoinsdialog.ui \
  forms/sendcoinsentry.ui \
  forms/signverifymessagedialog.ui \
  forms/transactiondescdialog.ui

QT_MOC_CPP = \
  moc_addressbookpage.cpp \
  moc_addresstablemodel.cpp \
  moc_askpassphrasedialog.cpp \
  moc_barnacoinaddressvalidator.cpp \
  moc_barnacoinamountfield.cpp \
  moc_barnacoingui.cpp \
  moc_barnacoinunits.cpp \
  moc_clientmodel.cpp \
  moc_coincontroldialog.cpp \
  moc_coincontroltreewidget.cpp \
  moc_csvmodelwriter.cpp \
  moc_editaddressdialog.cpp \
  moc_guiutil.cpp \
  moc_intro.cpp \
  moc_macdockiconhandler.cpp \
  moc_macnotificationhandler.cpp \
  moc_monitoreddatamapper.cpp \
  moc_notificator.cpp \
  moc_openuridialog.cpp \
  moc_optionsdialog.cpp \
  moc_optionsmodel.cpp \
  moc_overviewpage.cpp \
  moc_paymentserver.cpp \
  moc_qvalidatedlineedit.cpp \
  moc_qvaluecombobox.cpp \
  moc_receivecoinsdialog.cpp \
  moc_receiverequestdialog.cpp \
  moc_recentrequeststablemodel.cpp \
  moc_rpcconsole.cpp \
  moc_sendcoinsdialog.cpp \
  moc_sendcoinsentry.cpp \
  moc_signverifymessagedialog.cpp \
  moc_splashscreen.cpp \
  moc_trafficgraphwidget.cpp \
  moc_transactiondesc.cpp \
  moc_transactiondescdialog.cpp \
  moc_transactionfilterproxy.cpp \
  moc_transactiontablemodel.cpp \
  moc_transactionview.cpp \
  moc_utilitydialog.cpp \
  moc_walletframe.cpp \
  moc_walletmodel.cpp \
  moc_walletview.cpp

BARNACOIN_MM = \
  macdockiconhandler.mm \
  macnotificationhandler.mm

QT_MOC = \
  barnacoin.moc \
  intro.moc \
  overviewpage.moc \
  rpcconsole.moc

QT_QRC_CPP = qrc_barnacoin.cpp
QT_QRC = barnacoin.qrc

PROTOBUF_CC = paymentrequest.pb.cc
PROTOBUF_H = paymentrequest.pb.h
PROTOBUF_PROTO = paymentrequest.proto

BARNACOIN_QT_H = \
  addressbookpage.h \
  addresstablemodel.h \
  askpassphrasedialog.h \
  barnacoinaddressvalidator.h \
  barnacoinamountfield.h \
  barnacoingui.h \
  barnacoinunits.h \
  clientmodel.h \
  coincontroldialog.h \
  coincontroltreewidget.h \
  csvmodelwriter.h \
  editaddressdialog.h \
  guiconstants.h \
  guiutil.h \
  intro.h \
  macdockiconhandler.h \
  macnotificationhandler.h \
  monitoreddatamapper.h \
  notificator.h \
  openuridialog.h \
  optionsdialog.h \
  optionsmodel.h \
  overviewpage.h \
  paymentrequestplus.h \
  paymentserver.h \
  qvalidatedlineedit.h \
  qvaluecombobox.h \
  receivecoinsdialog.h \
  receiverequestdialog.h \
  recentrequeststablemodel.h \
  rpcconsole.h \
  sendcoinsdialog.h \
  sendcoinsentry.h \
  signverifymessagedialog.h \
  splashscreen.h \
  trafficgraphwidget.h \
  transactiondesc.h \
  transactiondescdialog.h \
  transactionfilterproxy.h \
  transactionrecord.h \
  transactiontablemodel.h \
  transactionview.h \
  utilitydialog.h \
  walletframe.h \
  walletmodel.h \
  walletmodeltransaction.h \
  walletview.h \
  winshutdownmonitor.h

RES_ICONS = \
  res/icons/add.png \
  res/icons/address-book.png \
  res/icons/barnacoin.ico \
  res/icons/barnacoin.png \
  res/icons/barnacoin_testnet.ico \
  res/icons/barnacoin_testnet.png \
  res/icons/clock1.png \
  res/icons/clock2.png \
  res/icons/clock3.png \
  res/icons/clock4.png \
  res/icons/clock5.png \
  res/icons/configure.png \
  res/icons/connect0_16.png \
  res/icons/connect1_16.png \
  res/icons/connect2_16.png \
  res/icons/connect3_16.png \
  res/icons/connect4_16.png \
  res/icons/debugwindow.png \
  res/icons/edit.png \
  res/icons/editcopy.png \
  res/icons/editpaste.png \
  res/icons/export.png \
  res/icons/filesave.png \
  res/icons/history.png \
  res/icons/key.png \
  res/icons/lock_closed.png \
  res/icons/lock_open.png \
  res/icons/overview.png \
  res/icons/qrcode.png \
  res/icons/quit.png \
  res/icons/receive.png \
  res/icons/remove.png \
  res/icons/send.png \
  res/icons/synced.png \
  res/icons/toolbar.png \
  res/icons/toolbar_testnet.png \
  res/icons/transaction0.png \
  res/icons/transaction2.png \
  res/icons/transaction_conflicted.png \
  res/icons/tx_inout.png \
  res/icons/tx_input.png \
  res/icons/tx_output.png \
  res/icons/tx_mined.png

BARNACOIN_QT_CPP = \
  barnacoin.cpp \
  barnacoinaddressvalidator.cpp \
  barnacoinamountfield.cpp \
  barnacoingui.cpp \
  barnacoinunits.cpp \
  clientmodel.cpp \
  csvmodelwriter.cpp \
  guiutil.cpp \
  intro.cpp \
  monitoreddatamapper.cpp \
  notificator.cpp \
  optionsdialog.cpp \
  optionsmodel.cpp \
  qvalidatedlineedit.cpp \
  qvaluecombobox.cpp \
  rpcconsole.cpp \
  splashscreen.cpp \
  trafficgraphwidget.cpp \
  utilitydialog.cpp \
  winshutdownmonitor.cpp

if ENABLE_WALLET
BARNACOIN_QT_CPP += \
  addressbookpage.cpp \
  addresstablemodel.cpp \
  askpassphrasedialog.cpp \
  coincontroldialog.cpp \
  coincontroltreewidget.cpp \
  editaddressdialog.cpp \
  openuridialog.cpp \
  overviewpage.cpp \
  paymentrequestplus.cpp \
  paymentserver.cpp \
  receivecoinsdialog.cpp \
  receiverequestdialog.cpp \
  recentrequeststablemodel.cpp \
  sendcoinsdialog.cpp \
  sendcoinsentry.cpp \
  signverifymessagedialog.cpp \
  transactiondesc.cpp \
  transactiondescdialog.cpp \
  transactionfilterproxy.cpp \
  transactionrecord.cpp \
  transactiontablemodel.cpp \
  transactionview.cpp \
  walletframe.cpp \
  walletmodel.cpp \
  walletmodeltransaction.cpp \
  walletview.cpp
endif

RES_IMAGES = \
  res/images/about.png \
  res/images/splash.png \
  res/images/splash_testnet.png

RES_MOVIES = $(wildcard res/movies/spinner-*.png)

BARNACOIN_RC = res/barnacoin-qt-res.rc

libbarnacoinqt_a_CPPFLAGS = $(AM_CPPFLAGS) $(QT_INCLUDES) \
  -I$(top_srcdir)/src/qt/forms $(QT_DBUS_INCLUDES)
libbarnacoinqt_a_SOURCES = $(BARNACOIN_QT_CPP) $(BARNACOIN_QT_H) $(QT_FORMS_UI) \
  $(QT_QRC) $(QT_TS) $(PROTOBUF_PROTO) $(RES_ICONS) $(RES_IMAGES) $(RES_MOVIES)

nodist_libbarnacoinqt_a_SOURCES = $(QT_MOC_CPP) $(QT_MOC) $(PROTOBUF_CC) \
  $(PROTOBUF_H) $(QT_QRC_CPP)

BUILT_SOURCES = $(nodist_libbarnacoinqt_a_SOURCES)

#Generating these with a half-written protobuf header leads to wacky results.
#This makes sure it's done.
$(QT_MOC): $(PROTOBUF_H)
$(QT_MOC_CPP): $(PROTOBUF_H)

# barnacoin-qt binary #
barnacoin_qt_CPPFLAGS = $(AM_CPPFLAGS) $(QT_INCLUDES) \
  -I$(top_srcdir)/src/qt/forms
barnacoin_qt_SOURCES = barnacoin.cpp
if TARGET_DARWIN
  barnacoin_qt_SOURCES += $(BARNACOIN_MM)
endif
if TARGET_WINDOWS
  barnacoin_qt_SOURCES += $(BARNACOIN_RC)
endif
barnacoin_qt_LDADD = libbarnacoinqt.a $(LIBBARNACOIN_SERVER)
if ENABLE_WALLET
barnacoin_qt_LDADD += $(LIBBARNACOIN_WALLET)
endif
barnacoin_qt_LDADD += $(LIBBARNACOIN_CLI) $(LIBBARNACOIN_COMMON) $(LIBLEVELDB) $(LIBMEMENV) \
  $(BOOST_LIBS) $(QT_LIBS) $(QT_DBUS_LIBS) $(QR_LIBS) $(PROTOBUF_LIBS) $(BDB_LIBS)
barnacoin_qt_LDFLAGS = $(QT_LDFLAGS)

# forms/foo.h -> forms/ui_foo.h
QT_FORMS_H=$(join $(dir $(QT_FORMS_UI)),$(addprefix ui_, $(notdir $(QT_FORMS_UI:.ui=.h))))

#locale/foo.ts -> locale/foo.qm
QT_QM=$(QT_TS:.ts=.qm)

.PHONY: FORCE
.SECONDARY: $(QT_QM)

barnacoinstrings.cpp: FORCE
	$(MAKE) -C $(top_srcdir)/src qt/barnacoinstrings.cpp

translate: barnacoinstrings.cpp $(QT_FORMS_UI) $(QT_FORMS_UI) $(BARNACOIN_QT_CPP) $(BARNACOIN_QT_H) $(BARNACOIN_MM)
	@test -n $(LUPDATE) || echo "lupdate is required for updating translations"
	@QT_SELECT=$(QT_SELECT) $(LUPDATE) $^ -locations relative -no-obsolete -ts locale/barnacoin_en.ts

$(QT_QRC_CPP): $(QT_QRC) $(QT_QM) $(QT_FORMS_H) $(RES_ICONS) $(RES_IMAGES) $(RES_MOVIES) $(PROTOBUF_H)
	@cd $(abs_srcdir); test -f $(RCC) && QT_SELECT=$(QT_SELECT) $(RCC) -name barnacoin -o $(abs_builddir)/$@ $< || \
	  echo error: could not build $@
	$(SED) -e '/^\*\*.*Created:/d' $@ > $@.n && mv $@{.n,}
	$(SED) -e '/^\*\*.*by:/d' $@  > $@.n && mv $@{.n,}

CLEANFILES = $(BUILT_SOURCES) $(QT_QM) $(QT_FORMS_H) *.gcda *.gcno
